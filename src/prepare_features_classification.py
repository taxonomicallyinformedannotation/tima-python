#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""You can use this script with the following example:
python prepare_features_classification.py --input 'data/interim/annotations/db1c51fa29a64892af520698a18783e4_isdb_filled.tsv.gz' --output 'data/interim/annotations/db1c51fa29a64892af520698a18783e4_isdb_treated.tsv.gz' --library 'data/interim/libraries/library.tsv.gz' --quickmode TRUE

Usage: prepare_features_classification.py [--input=<input>] [--output=<output>] [--library=<library>]

Arguments:
  -i --input=<input>            Your isdb result file. Supports compressed files.
  -o --output=<output>          Path and filename for the output. If you specify .gz file will be compressed.
  -q --quickmode=<quickmode>    Boolean. Do you want to classify only with LOTUS (quick) or submit to GNPS (long)?
  -t --tool=<tool>              Tool used for generating the component ids, currently only GNPS

Options:
  -h --help                     Show this screen.
  -v --version                  Show version.

"""

import os

import pandas
from docopt import docopt

from helpers.get_params import get_params
from helpers.parse_yaml_paths import parse_yaml_paths

if __name__ == '__main__':
    arguments = docopt(__doc__)

step = 'prepare_features_classification'

paths = parse_yaml_paths()

params = get_params(step=step, cli=arguments)

print('Loading ...')
if os.path.isfile(params["library"]):
    col_list = [
        'structure_inchikey_2D',
        'structure_smiles_2D',
        'structure_exact_mass',
        'structure_molecular_formula',
        'structure_taxonomy_npclassifier_01pathway',
        'structure_taxonomy_npclassifier_02superclass',
        'structure_taxonomy_npclassifier_03class'
    ]
    print('... library')
    library = pandas.read_csv(
        filepath_or_buffer=params["library"],
        usecols=col_list
    ).rename(
        columns={
            'structure_inchikey_2D': 'inchikey_2D',
            'structure_smiles_2D': 'smiles_2D',
            'structure_exact_mass': 'exact_mass',
            'structure_molecular_formula': 'molecular_formula'
        }
    ).drop_duplicates()
else:
    print("""Sorry, wrong file path""")

if os.path.isfile(params["input"]):
    print('... feature table with components')
    table = pandas.read_csv(
        filepath_or_buffer=params["input"]
    )
else:
    print("""Sorry, wrong file path""")

print('Filtering structures ...')
print('... missing classification')
table_missing_classification = table[[
    "inchikey_2D",
    "smiles_2D",
    "structure_taxonomy_npclassifier_01pathway",
    "structure_taxonomy_npclassifier_02superclass",
    "structure_taxonomy_npclassifier_03class"]].drop_duplicates()[
    pandas.isnull(table['structure_taxonomy_npclassifier_01pathway']) &
    pandas.isnull(table['structure_taxonomy_npclassifier_02superclass']) &
    pandas.isnull(table['structure_taxonomy_npclassifier_03class'])
    ].drop(columns=[
    'structure_taxonomy_npclassifier_01pathway',
    'structure_taxonomy_npclassifier_02superclass',
    'structure_taxonomy_npclassifier_03class'
])

print('... missing mass')
table_missing_mass = table[[
    "inchikey_2D",
    "smiles_2D",
    "structure_exact_mass"]].drop_duplicates()[
    pandas.isnull(table['structure_exact_mass'])
].drop(columns=['structure_exact_mass'])

print('... missing formula')
table_missing_formula = table[[
    "inchikey_2D",
    "smiles_2D",
    "molecular_formula"]].drop_duplicates()[
    pandas.isnull(table['molecular_formula'])
].drop(columns=['molecular_formula'])

print('... keeping the other ones safe')
table_with_classification = table.drop(table.merge(table_missing_classification).index)
table_with_mass = table.drop(table.merge(table_missing_mass).index)
table_with_formula = table.drop(table.merge(table_missing_formula).index)

print('Completing structures with the library ...')
print('... classification')
table_classified_lotus = table_missing_classification.merge(library[[
    "inchikey_2D",
    "smiles_2D",
    'structure_taxonomy_npclassifier_01pathway',
    'structure_taxonomy_npclassifier_02superclass',
    'structure_taxonomy_npclassifier_03class'
]].drop_duplicates())

print('... mass')
table_massed_lotus = table_missing_mass.merge(library[[
    "inchikey_2D",
    "smiles_2D",
    "exact_mass"]].drop_duplicates())

print('... formula')
table_formuled_lotus = table_missing_formula.merge(library[[
    "inchikey_2D",
    "smiles_2D",
    "molecular_formula"]].drop_duplicates())

print('Calculating what is missing WARNING: NOT DONE YET, WILL BE IMPLEMENTED SOON')
# TODO add calculations step for missing ones (and preparation of missing ones)

print('Recombining everything back together')
table_classified = pandas.concat([table_with_classification[[
    'inchikey_2D',
    'smiles_2D',
    'structure_taxonomy_npclassifier_01pathway',
    'structure_taxonomy_npclassifier_02superclass',
    'structure_taxonomy_npclassifier_03class'
]].drop_duplicates(), table_classified_lotus])

print(table_classified)
table_massed = pandas.concat([table_with_mass[[
    'inchikey_2D',
    'smiles_2D',
    'structure_exact_mass'
]].drop_duplicates(), table_massed_lotus]).drop(columns=['exact_mass'])
print(table_massed)

table_formuled = pandas.concat([table_with_formula[[
    'inchikey_2D',
    'smiles_2D',
    'molecular_formula'
]].drop_duplicates(), table_formuled_lotus])
print(table_formuled)

table_final = table[[
    'feature_id',
    'component_id',
    'mz',
    'rt',
    'inchikey_2D',
    'smiles_2D',
    'score_input',
    'library',
    'mz_error']].drop_duplicates(
).merge(table_classified
        ).merge(table_massed
                ).merge(table_formuled)

print('Exporting features with components and metadata')
os.makedirs(os.path.dirname(params["output"]), exist_ok=True)
table_final.to_csv(
    path_or_buf=params["output"],
    index=False
)

export_params(
    parameters=params,
    directory=paths["data"]["interim"]["config"]["path"],
    step=step)
