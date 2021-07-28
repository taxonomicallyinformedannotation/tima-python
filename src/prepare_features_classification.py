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

from helpers.export_params import export_params
from helpers.get_params import get_params
from helpers.parse_yaml_paths import parse_yaml_paths

if __name__ == '__main__':
    arguments = docopt(__doc__)

step = 'prepare_features_classification'

paths = parse_yaml_paths()

params = get_params(step=step, cli=arguments)

if os.path.isfile(params["input"]):
    print('bla')

    file_initial = pandas.read_csv(
        filepath_or_buffer=params["input"]
    )

    export_params(
        parameters=params,
        directory=paths["data"]["interim"]["config"]["path"],
        step=step)

else:
    print("""Sorry, wrong file path""")
