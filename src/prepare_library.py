#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This script prepares a single library with all prepared libraries \n,
   for further processing"""

import glob
import os

import pandas

from helpers.parse_yaml_params import parse_yaml_params
from helpers.parse_yaml_paths import parse_yaml_paths

paths = parse_yaml_paths()

params = parse_yaml_params(step="prepare_library")

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

# TODO export params when modified with CLI
