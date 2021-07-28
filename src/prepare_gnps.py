#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""You can use this script with the following example:
python prepare_gnps.py -o 'data/interim/db1c51fa29a64892af520698a18783e4_gnps_pretreated.tsv.gz' -g db1c51fa29a64892af520698a18783e4

Usage: prepare_gnps.py [--output=<output>] [--nap=<nap>] [--gnps=<gnps>]

Arguments:
  -o --output=<output>  Path and filename for the output. If you specify .gz file will be compressed.
  -n --nap=<nap>        Your NAP job id.
  -g --gnps=<gnps>      Your GNPS job id.

Options:
  -h --help          Show this screen.
  -v --version       Show version.

"""

from docopt import docopt

from helpers.export_params import export_params
from helpers.get_gnps import read_results
from helpers.get_params import get_params
from helpers.parse_yaml_paths import parse_yaml_paths

if __name__ == '__main__':
    arguments = docopt(__doc__)

step = 'prepare_gnps'

paths = parse_yaml_paths()

params = get_params(step=step, cli=arguments)

print('Loading GNPS results')
results_table = read_results(gnps=params["gnps"])

print('Formatting GNPS results')
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

print('Exporting GNPS results')
results_table_treated.to_csv(
    path_or_buf=params["output"],
    index=False
)

export_params(
    parameters=params,
    directory=paths["data"]["interim"]["config"]["path"],
    step=step)
