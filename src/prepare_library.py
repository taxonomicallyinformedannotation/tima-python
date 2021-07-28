#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""You can use this script with the following example:
python prepare_library.py --output 'bitter_db.tsv.gz' --filter TRUE --level 'family' --value 'Simaroubaceae|Gentianaceae'

Usage: prepare_library.py [--output=<output>] [--filter=<filter>] [--level=<level>] [--value=<value>] 

Arguments:
  -f --filter=<filter>  Boolean. If you want to filter your library for specific organisms
  -l --level=<level>    The taxonomic level you want to filter. Must be one of {domain, kingdom, phylum, class, order, family, tribe, genus, species, varietas}
  -v --value=<value>    The value of your filter. (eg. "Gentianaceae", can be OR in form of "Simaroubaceae|Gentianaceae")
  -o --output=<output>  Filename for the output.

Options:
  -h --help         Show this screen.
  -V --version      Show version.

"""

import glob
import os

import pandas
from docopt import docopt

from helpers.export_params import export_params
from helpers.get_params import get_params
from helpers.parse_yaml_paths import parse_yaml_paths

if __name__ == '__main__':
    arguments = docopt(__doc__)

step = 'prepare_library'

paths = parse_yaml_paths()

params = get_params(step=step, cli=arguments)

all_files = glob.glob(
    paths["data"]["interim"]["libraries"]["path"] +
    "/*_prepared.tsv.gz"
)

df = pandas.concat((pandas.read_csv(f) for f in all_files))

if params["filter"]["mode"]:
    df = df[df.columns.str.contains(
        pat=params["filter"]["value"]
    ) == params["filter"]["level"]]

else:
    print("""Great, a comprehensive library""")

df.to_csv(
    path_or_buf=os.path.join(
        paths["data"]["interim"]["libraries"]["path"],
        params["output"]
    ),
    index=False
)

export_params(
    parameters=params,
    directory=paths["data"]["interim"]["config"]["path"],
    step=step)
