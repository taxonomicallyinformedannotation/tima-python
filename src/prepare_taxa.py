#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This script prepares taxa"""

import os
from sys import exit

import pandas

from helpers.get_gnps import read_features
from helpers.get_gnps import read_metadata
from helpers.parse_yaml_params import parse_yaml_params
from helpers.parse_yaml_paths import parse_yaml_paths
from preprocessing.taxa.clean_gnverifier import clean_gnverifier
from preprocessing.taxa.manipulating_taxo_otl import manipulating_taxo_otl

paths = parse_yaml_paths()

params = parse_yaml_params(step="prepare_taxa")

if params["tool"] in ['gnps', 'manual']:
    print("""Tool parameter OK""")
else:
    print(
        """Your --tool.metadata parameter (in command line arguments or in 'inform_params.yaml' must be either 'gnps' or 'manual'""")
    exit()

if params["top_k"] <= 5:
    print("""Top K parameter OK""")
else:
    print(
        """Your --top_k.organism_per_feature parameter (in command line arguments or in 'inform_params.yaml' should be lower or equal to 5""")
    exit()

taxa_ranks_dictionary = pandas.read_csv(
    filepath_or_buffer=paths["data"]["source"]["dictionaries"]["ranks"]
)

if params["tool"] == 'gnps':
    feature_table = read_features(gnps=params["gnps"]).filter(
        regex='(row ID)|( Peak area)'
    )
    metadata_table = read_metadata(gnps=params["gnps"])

    feature_table.columns = feature_table.columns.str.rstrip(' Peak area')

    feature_table = pandas.melt(
        feature_table,
        id_vars=['row ID']
    )

    feature_table = feature_table[feature_table['value'] != 0]

    feature_table["rank"] = feature_table.groupby(
        "row ID")["value"].rank(
        "dense", ascending=False)

    feature_table = feature_table[feature_table['rank'] <= params["top_k"]]

    ## TODO manual possibility to add

    organism_table = metadata_table[params["column_name"]].drop_duplicates()

    organism_table.to_csv(
        path_or_buf=paths["data"]["interim"]["taxa"]["original"],
        index=False
    )

    print('Submitting to GNVerifier')

    os.system(
        'bash' + " " + paths["src"]["gnverifier"]
    )

    dataOrganismVerified_3 = clean_gnverifier(file=paths["data"]["interim"]["taxa"]["verified"])

    organism_cleaned_manipulated = manipulating_taxo_otl(dataOrganismVerified_3)

    if not params["extension"]:
        metadata_table.filename = metadata_table.filename.str.rstrip('.mzML')
        metadata_table.filename = metadata_table.filename.str.rstrip('.mzxML')

    metadata_table_joined = feature_table.set_index(
        'variable').join(
        metadata_table.set_index(
            'filename'))[['row ID', params["column_name"]]].rename(
        columns={
            'row ID': 'feature_id',
            params["column_name"]: 'organismOriginal'
        }
    ).merge(
        organism_cleaned_manipulated
    ).drop(
        columns={
            'organismOriginal',
            'organismCleaned'
        })

    metadata_table_joined_summarized = metadata_table_joined.groupby(
        "feature_id").agg(
        lambda x: '|'.join(
            {elem for elem in x if ~pandas.isnull(elem)})).reset_index()

    metadata_table_joined_summarized.to_csv(
        path_or_buf=params["output"],
        index=False
    )

else:
    print("""manual version still to do, Sorry""")

## TODO export params when modified with CLI
