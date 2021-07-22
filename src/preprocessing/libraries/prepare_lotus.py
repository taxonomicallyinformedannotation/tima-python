#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This script prepares LOTUS referenced structure-organism pairs \n,
   for further processing"""

import pandas
import yaml

with open("paths.yaml", 'r') as stream:
    try:
        paths = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

file_initial = pandas.read_csv(paths["data"]["source"]["libraries"]["lotus"])

file_formatted = file_initial.assign(structure_inchikey_2D=file_initial.structure_inchikey.str[0:13])[[
    # 'structure_name',
    'structure_inchikey_2D',
    'structure_smiles_2D',
    'structure_molecular_formula',
    'structure_exact_mass',
    # 'structure_xlogp',
    'structure_taxonomy_npclassifier_01pathway',
    'structure_taxonomy_npclassifier_02superclass',
    'structure_taxonomy_npclassifier_03class',
    'organism_name', 'organism_taxonomy_01domain',
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
    'reference_doi']].drop_duplicates()

file_formatted.to_csv(paths["data"]["interim"]["libraries"]["lotus"])
