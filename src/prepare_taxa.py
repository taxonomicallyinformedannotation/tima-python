#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""You can use this script with the following example:
python prepare_taxa.py --output 'data/interim/taxa/db1c51fa29a64892af520698a18783e4_taxed.tsv.gz' --tool gnps --k.top 1 --column.name 'ATTRIBUTE_species' --extension FALSE

Usage: prepare_taxa.py [--input=<input>] [--output=<output>] [--tool=<tool>] [--column.name=<column.name>] [--gnps=<gnps>] [--k.top=<k.top>]

Options:
  -c --column.name=<column.name>  Name of the column containing the lowest possible taxon in your feature file.
  -e --extension=<extension>      Is the filename extension in your feature table? Boolean
  -g --gnps=<gnps>                Your GNPS job id. Depending on the annotation tool you used
  -i --input=<input>              File containing your intensity/sample to attribute biological source. Supports compressed files.
  -k --k.top=<k.top>              Number of allowed biological sources per feature. Should not exceed 5.
  -o --output=<output>            Path and filename for the output. If you specify .gz file will be compressed.
  -t --tool=<tool>                Tool you used for your metadata organization ('gnps' and 'manual' currently supported)
  -h --help                       Show this screen.
  -v --version                    Show version.

"""

import os
from sys import exit

import pandas
from docopt import docopt

from helpers.export_params import export_params
from helpers.get_gnps import read_features
from helpers.get_gnps import read_metadata
from helpers.get_params import get_params
from helpers.parse_yaml_paths import parse_yaml_paths
from preprocessing.taxa.clean_gnverifier import clean_gnverifier
from preprocessing.taxa.manipulating_taxo_otl import manipulating_taxo_otl

if __name__ == '__main__':
    arguments = docopt(__doc__)

step = 'prepare_taxa'

paths = parse_yaml_paths()

params = get_params(step=step, cli=arguments)

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

    export_params(
        parameters=params,
        directory=paths["data"]["interim"]["config"]["path"],
        step=step)

else:
    print("""manual version still to do, Sorry""")
