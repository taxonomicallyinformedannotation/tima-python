#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This script prepares LOTUS referenced structure-organism pairs \n,
   for further processing"""

import pandas

from helpers.parse_yaml_paths import parse_yaml_paths

paths = parse_yaml_paths()

print('Loading LOTUS library')
col_list = [
    # 'structure_name',
    # 'structure_inchikey_2D',
    'structure_inchikey',
    'structure_smiles_2D',
    'structure_molecular_formula',
    'structure_exact_mass',
    # 'structure_xlogp',
    'structure_taxonomy_npclassifier_01pathway',
    'structure_taxonomy_npclassifier_02superclass',
    'structure_taxonomy_npclassifier_03class',
    'organism_name',
    'organism_taxonomy_01domain',
    'organism_taxonomy_02kingdom',
    'organism_taxonomy_03phylum',
    'organism_taxonomy_04class',
    'organism_taxonomy_05order',
    'organism_taxonomy_06family',
    'organism_taxonomy_07tribe',
    'organism_taxonomy_08genus',
    'organism_taxonomy_09species',
    'organism_taxonomy_10varietas',
    # 'reference_title',
    'reference_doi'
]
file_initial = pandas.read_csv(
    filepath_or_buffer=paths["data"]["source"]["libraries"]["lotus"],
    usecols=col_list
)

print('Minimal formatting...')
file_formatted = file_initial.assign(
    structure_inchikey_2D=file_initial.structure_inchikey.str[0:14]
).drop(
    columns='structure_inchikey'
).drop_duplicates()

print('Exporting LOTUS library')
file_formatted.to_csv(
    path_or_buf=paths["data"]["interim"]["libraries"]["lotus"],
    index=False
)
