#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This script prepares DNP structure-organism pairs \n,
   for further processing"""

import os

import pandas

from helpers.parse_yaml_params import parse_yaml_params
from helpers.parse_yaml_paths import parse_yaml_paths

paths = parse_yaml_paths()

params = parse_yaml_params(step="prepare_dnp")

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

## TODO export params when modified with CLI

else:
    print("""Sorry, you do not have access to the DNP""")
