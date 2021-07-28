#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

import pandas


def preclean_gnverifier(file):
    verified = []
    print("Loading GNVerifier results")
    with open(file) as f:
        for jsonObj in f:
            Dict = json.loads(jsonObj)
            verified.append(Dict)

        print("Formatting GNVerifier results")
        verified_df = pandas.DataFrame.from_records(
            verified
        ).drop(
            ['curation', 'matchType'], axis=1
        ).explode(
            'preferredResults'
        )
        df2 = verified_df.preferredResults.apply(pandas.Series)  ## this could be 1400x faster
        df3 = df2.rename(
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
        dataOrganismVerified = verified_df.join(df3)[[
            'input',
            'organismCleaned',
            'organismDbTaxo',
            'taxonId',
            'organismCleanedCurrent',
            'organismCleaned_dbTaxoTaxonomy',
            'organismCleaned_dbTaxoTaxonRanks'
        ]].drop_duplicates()
        return (dataOrganismVerified)
