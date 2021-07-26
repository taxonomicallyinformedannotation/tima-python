#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

import pandas


def preclean_gnverifier(file):
    verified = []
    print("Started Reading JSON file which contains multiple JSON document")
    with open(file) as f:
        for jsonObj in f:
            Dict = json.loads(jsonObj)
            verified.append(Dict)
        verified_df = pandas.DataFrame.from_records(
            verified
        ).drop(
            ['curation', 'matchType'], axis=1
        ).explode(
            'preferredResults'
        )
        df2 = verified_df.preferredResults.apply(pandas.Series)  ## this could be 1400x faster
        df3 = df2[df2.dataSourceTitleShort == "Open Tree of Life"]
        df4 = df3.rename(
            columns={
                'currentCanonicalFull': 'organismCleaned',
                'dataSourceTitleShort': 'organismDbTaxo',
                'currentRecordId': 'taxonId',
                'currentName': 'organismCleanedCurrent',
                'classificationPath': 'organismCleaned_dbTaxoTaxonomy',
                'classificationRanks': 'organismCleaned_dbTaxoTaxonRanks'
            }
        )[[
            'organismCleaned',
            'organismDbTaxo',
            'taxonId',
            'organismCleanedCurrent',
            'organismCleaned_dbTaxoTaxonomy',
            'organismCleaned_dbTaxoTaxonRanks'
        ]]
        dataOrganismVerified = verified_df.join(df4)[[
            'input',
            'organismCleaned',
            'organismDbTaxo',
            'taxonId',
            'organismCleanedCurrent',
            'organismCleaned_dbTaxoTaxonomy',
            'organismCleaned_dbTaxoTaxonRanks'
        ]].drop_duplicates()
        return (dataOrganismVerified)
