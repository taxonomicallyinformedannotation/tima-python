#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This script prepares ISDB results"""

import os

import pandas

from helpers.parse_yaml_params import parse_yaml_params
from helpers.parse_yaml_paths import parse_yaml_paths

paths = parse_yaml_paths()

params = parse_yaml_params(step="prepare_isdb")

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

else:
    print("""Sorry, wrong file path""")
