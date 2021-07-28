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

import os

import pandas
from docopt import docopt

from helpers.export_params import export_params
from helpers.get_params import get_params
from helpers.parse_yaml_paths import parse_yaml_paths

if __name__ == '__main__':
    arguments = docopt(__doc__)

step = 'prepare_features_components'

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
