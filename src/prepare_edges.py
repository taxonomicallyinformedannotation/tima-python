#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""You can use this script with the following example:
python prepare_edges.py --input 'data/source/example_edges_manual.csv' --output 'data/interim/edges/db1c51fa29a64892af520698a18783e4_edges.tsv.gz' --tool gnps

Usage: prepare_edges.py [--input=<input>] [--output=<output>] [--tool=<tool>] [--gnps=<gnps>] [-1 | --source=<source>] [-2 | --target=<target>]

Options:
  -i --input=<input>                    If manual, your file containing list of edges between features. Supports compressed files.
  -g --gnps=<gnps>                      Your GNPS job id. Depending on the annotation tool you used
  -o --output=<output>                  Path and filename for the output. If you specify .gz file will be compressed.
  -t --tool=<tool>                      Tool you used for edge generation ('gnps' or 'manual')
  -1 --source=<source>                  The column name of your source feature
  -2 --target=<target>                  The column name of your target feature
  -h --help                             Show this screen.
  -v --version                          Show version.

"""
import os

from docopt import docopt

from helpers.export_params import export_params
from helpers.get_gnps import read_edges
from helpers.get_params import get_params
from helpers.parse_yaml_paths import parse_yaml_paths

if __name__ == '__main__':
    arguments = docopt(__doc__)

step = 'prepare_edges'

paths = parse_yaml_paths()

params = get_params(step=step, cli=arguments)

if params["tool"] == 'gnps':

    print('Loading edges table')
    edges_table = read_edges(gnps=params["gnps"])

    print('Formatting edges table')
    edges_table_treated = edges_table.rename(
        columns={
            params["source_name"]: 'feature_source',
            params["target_name"]: 'feature_target'
        }
    )[['feature_source', 'feature_target']].query(
        'feature_source != feature_target'
    )

    print('Exporting edges table')
    os.makedirs(os.path.dirname(params["output"]), exist_ok=True)
    edges_table_treated.to_csv(
        path_or_buf=params["output"],
        index=False
    )

    export_params(
        parameters=params,
        directory=paths["data"]["interim"]["config"]["path"],
        step=step)

else:
    # TODO manual possibility to add
    print("""manual version still to do, Sorry""")
