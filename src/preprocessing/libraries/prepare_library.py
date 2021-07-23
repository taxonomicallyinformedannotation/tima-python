#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This script prepares a single library with all prepared libraries \n,
   for further processing"""

import glob
import os

import pandas
import yaml

with open("paths.yaml", 'r') as stream:
    try:
        paths = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

os.chdir(paths["base_dir"])

with open("config/default/prepare_library.yaml", 'r') as stream:
    try:
        params = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

with open("config/params/prepare_library.yaml", 'r') as stream:
    try:
        params = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

all_files = glob.glob(
    paths["data"]["interim"]["libraries"]["path"] +
    "/*_prepared.tsv.gz"
)

df = pandas.concat((pandas.read_csv(f) for f in all_files))

if (params["filter"]["mode"]):
    df = df[df.columns.str.contains(
        pat=params["filter"]["level"]
    ) == params["filter"]["value"]]

else:
    print("""Great, a comprehensive library""")

df.to_csv(
    path_or_buf=os.path.join(
        paths["data"]["interim"]["libraries"]["path"],
        params["output"]
    )
)
