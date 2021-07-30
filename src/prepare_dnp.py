#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""You can use this script with the following example:
python prepare_dnp.py --input '../lotus-processor/data/processed/210715_dnp_metadata.csv.gz' 

Usage: prepare_dnp.py [--input=<input>] [--output=<output>]

Arguments:
  -i --input=<input>    Where your dnp is located. Works only with special in lab dnp. Cannot be shared
  -o --output=<output>  Output

Options:
  -h --help             Show this screen.
  -V --version          Show version.

"""

import os

import pandas
from docopt import docopt

from helpers.export_params import export_params
from helpers.get_params import get_params
from helpers.parse_yaml_paths import parse_yaml_paths

if __name__ == '__main__':
    arguments = docopt(__doc__)

step = 'prepare_dnp'

paths = parse_yaml_paths()

params = get_params(step=step, cli=arguments)

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

    print('Loading DNP')
    file_initial = pandas.read_csv(
        filepath_or_buffer=params["input"],
        usecols=col_list
    )

    print('Formatting DNP')
    file_formatted = \
        file_initial.assign(
            structure_inchikey_2D=file_initial.structure_inchikey.str[0:14],
            reference_doi=""
        ).drop_duplicates(

        )

    print('Exporting DNP')
    os.makedirs(os.path.dirname(params["output"]), exist_ok=True)
    file_formatted.to_csv(
        path_or_buf=params["output"],
        index=False
    )

    export_params(
        parameters=params,
        directory=paths["data"]["interim"]["config"]["path"],
        step=step)

else:
    print("""Sorry, you do not have access to the DNP""")
