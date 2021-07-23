#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This script prepares adducts from the \n,
   structure-organism pairs for further processing"""

import os

import pandas
import yaml

with open("paths.yaml", 'r') as stream:
    try:
        paths = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

os.chdir(paths["base_dir"])

with open("config/default/prepare_adducts.yaml", 'r') as stream:
    try:
        params = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

with open("config/params/prepare_adducts.yaml", 'r') as stream:
    try:
        params = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

col_list = ["structure_exact_mass"]

if os.path.isfile(params["input"]):
    masses = pandas.read_csv(
        filepath_or_buffer=params["input"],
        usecols=col_list
    ).rename(
        columns={"structure_exact_mass": "exact_mass"}
    )

    adducts = pandas.read_csv(
        filepath_or_buffer=paths["data"]["source"]["adducts"], sep='\t'
    ).transpose(

    )

    adducts.columns = adducts.iloc[0]

    adducts = adducts.filter(
        like='mass', axis=0)

    print(adducts)

    masses_adducts = pandas.concat(
        objs=[masses.reset_index(drop=True),
              adducts.reset_index(drop=True)],
        ignore_index=True,
        axis=1
    ).ffill(
        axis=0
    )

    print(masses_adducts)

# to continue...

else:
    print("""Sorry, your path does not match any file""")
