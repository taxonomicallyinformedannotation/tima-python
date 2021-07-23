#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This script prepares DNP structure-organism pairs \n,
   for further processing"""

import os

import pandas
import yaml

with open("paths.yaml", 'r') as stream:
    try:
        paths = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

os.chdir(paths["base_dir"])

with open("config/default/prepare_dnp.yaml", 'r') as stream:
    try:
        params = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

with open("config/params/prepare_dnp.yaml", 'r') as stream:
    try:
        params = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

if os.path.isfile(params["input"]):
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
        # 'reference_doi'
    ]

    file_initial = pandas.read_csv(
        filepath_or_buffer=params["input"],
        usecols=col_list
    )

    file_formatted = \
        file_initial.assign(
            structure_inchikey_2D=file_initial.structure_inchikey.str[0:13],
            reference_doi=""
        ).drop_duplicates(

        )

    file_formatted.to_csv(
        path_or_buf=params["output"],
        index=False
    )

else:
    print("""Sorry, you do not have access to the DNP""")
