#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""You can use this script with the following example:
python prepare_isdb.py --input 'data/interim/annotations/example_isdb_result.tsv.gz' --output 'data/interim/annotations/db1c51fa29a64892af520698a18783e4_isdb_pretreated.tsv.gz'

Usage: prepare_isdb.py [--input=<input>] [--output=<output>]

Arguments:
  -i --input=<input>    Your isdb result file. Supports compressed files.
  -o --output=<output>  Path and filename for the output. If you specify .gz file will be compressed.

Options:
  -h --help         Show this screen.
  -v --version      Show version.

"""

import os

import pandas
from docopt import docopt

from helpers.export_params import export_params
from helpers.get_params import get_params
from helpers.parse_yaml_paths import parse_yaml_paths

if __name__ == '__main__':
    arguments = docopt(__doc__)

step = 'prepare_isdb'

paths = parse_yaml_paths()

params = get_params(step=step, cli=arguments)

if os.path.isfile(params["input"]):
    results_table = pandas.read_csv(
        filepath_or_buffer=params["input"]
    )

    results_table_treated = results_table.rename(
        columns={
            'short_inchikey': 'inchikey_2D',
            'exact_mass': 'structure_exact_mass',
            'msms_score': 'score_input'
        }
    )

    results_table_treated['library'] = 'ISDB'
    results_table_treated['inchikey'] = ''
    results_table_treated['smiles_2D'] = results_table_treated['smiles']
    results_table_treated['structure_taxonomy_npclassifier_01pathway'] = ''
    results_table_treated['structure_taxonomy_npclassifier_02superclass'] = ''
    results_table_treated['structure_taxonomy_npclassifier_03class'] = ''

    results_table_treated = results_table_treated[[
        'feature_id',
        'smiles',
        'inchikey',
        'inchikey_2D',
        'structure_taxonomy_npclassifier_01pathway',
        'structure_taxonomy_npclassifier_02superclass',
        'structure_taxonomy_npclassifier_03class',
        'structure_exact_mass',
        'score_input',
        'library',
        'smiles_2D',
        'molecular_formula'
    ]]

    results_table_treated.to_csv(
        path_or_buf=params["output"],
        index=False
    )

    export_params(
        parameters=params,
        directory=paths["data"]["interim"]["config"]["path"],
        step=step)

else:
    print("""Sorry, wrong file path""")
