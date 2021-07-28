#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""You can use this script with the following example:
python prepare_features_components.py --input 'data/interim/annotations/db1c51fa29a64892af520698a18783e4_isdb_pretreated.tsv.gz' --output 'data/interim/annotations/db1c51fa29a64892af520698a18783e4_isdb_filled.tsv.gz' --mode 'pos' --tool 'gnps' --gnps 'db1c51fa29a64892af520698a18783e4'

Usage: prepare_features_components.py [--input=<input>] [--output=<output>] [--mode=<mode>]

Arguments:
  -c --components=<components>  If your tool is manual, the file containing your component_ids
  -g --gnps=<gnps>              GNPS job ID.
  -i --input=<input>            Your isdb result file. Supports compressed files.
  -o --output=<output>          Path and filename for the output. If you specify .gz file will be compressed.
  -m --mode=<mode>              MS mode used. Can be "pos" or "neg"
  -t --tool=<tool>              Tool used for generating the component ids, currently only GNPS

Options:
  -h --help                     Show this screen.
  -v --version                  Show version.

"""

import pandas
from docopt import docopt

from helpers.export_params import export_params
from helpers.get_gnps import read_clusters
from helpers.get_params import get_params
from helpers.parse_yaml_paths import parse_yaml_paths

if __name__ == '__main__':
    arguments = docopt(__doc__)

step = 'prepare_features_components'

paths = parse_yaml_paths()

params = get_params(step=step, cli=arguments)

print('Loading ...')
print('... features table')
features_table = pandas.read_csv(
    filepath_or_buffer=params["input"]
)

if params["tool"] == 'gnps':
    components_table = read_clusters(gnps=params["gnps"])

    print('THIS STEP CAN BE IMPROVED BY CALCULATING THE CLUSTERS WITHIN SPEC2VEC')

    print('Formatting components')
    components_table_treated = components_table.rename(
        columns={
            'cluster index': 'feature_id',
            'componentindex': 'component_id',
            'RTMean': 'rt',
            'precursor mass': 'mz'
        }
    )

    print('Adding components to features')
    components_table_treated = components_table_treated.merge(
        features_table).drop_duplicates(
    )[[
        'feature_id',
        'component_id',
        'rt',
        'mz',
        'inchikey_2D',
        'smiles_2D',
        'molecular_formula',
        'exact_mass',
        'score_input',
        'library',
        'structure_taxonomy_npclassifier_01pathway',
        'structure_taxonomy_npclassifier_02superclass',
        'structure_taxonomy_npclassifier_03class'
    ]]

    print('Calculating m/z error')
    # TODO can be improved
    if params["mode"] == 'neg':
        table_filled = components_table_treated.assign(
            mz_error=(components_table_treated['mz'] + 1.007276 - components_table_treated['structure_exact_mass'])
        )
    else:
        table_filled = components_table_treated.assign(
            mz_error=(components_table_treated['mz'] - 1.007276 - components_table_treated['structure_exact_mass'])
        )

    print('Exporting features with components')
    os.makedirs(os.path.dirname(params["output"]), exist_ok=True)
    table_filled.to_csv(
        path_or_buf=params["output"],
        index=False
    )

    export_params(
        parameters=params,
        directory=paths["data"]["interim"]["config"]["path"],
        step=step)

else:
    print("""Sorry, wrong file path""")
