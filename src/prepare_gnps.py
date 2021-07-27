#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This script prepares GNPS results"""

from helpers.get_gnps import read_results
from helpers.parse_yaml_params import parse_yaml_params
from helpers.parse_yaml_paths import parse_yaml_paths

paths = parse_yaml_paths()

params = parse_yaml_params(step="prepare_gnps")

results_table = read_results(gnps=params["gnps"])

results_table_treated = results_table.rename(
    columns={
        '#Scan#': 'feature_id',
        'Smiles': 'smiles',
        'InChIKey': 'inchikey',
        'InChIKey-Planar': 'inchikey_2D',
        'npclassifier_pathway': 'structure_taxonomy_npclassifier_01pathway',
        'npclassifier_superclass': 'structure_taxonomy_npclassifier_02superclass',
        'npclassifier_class': 'structure_taxonomy_npclassifier_03class',
        'ExactMass': 'structure_exact_mass',
        'MQScore': 'score_input'
    }
)

results_table_treated['library'] = 'GNPS'
results_table_treated['smiles_2D'] = ''
results_table_treated['molecular_formula'] = ''

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
