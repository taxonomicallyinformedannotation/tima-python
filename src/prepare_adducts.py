#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""You can use this script with the following example:
python prepare_adducts.py --input data/interim/libraries/library.tsv.gz --output library

Usage: prepare_adducts.py [--input=<input>] [--output=<output>]

Arguments:
  -i --input=<input>    Path to the input. Starting from root of the directory
  -o --output=<output>  Filename for the outputs. "_pos" and "_neg" will be appended.

Options:
  -h --help         Show this screen.
  -V --version      Show version.

"""

import os

import pandas
from docopt import docopt

from helpers.export_params import export_params
from helpers.get_params import get_params
from helpers.parse_yaml_paths import parse_yaml_paths
from preprocessing.libraries.adducts.form_adducts_neg import form_adducts_neg
from preprocessing.libraries.adducts.form_adducts_pos import form_adducts_pos

if __name__ == '__main__':
    arguments = docopt(__doc__)

step = 'prepare_adducts'
paths = parse_yaml_paths()

params = get_params(step=step, cli=arguments)

col_list = ["structure_exact_mass"]

if os.path.isfile(params["input"]):
    masses = pandas.read_csv(
        filepath_or_buffer=params["input"],
        usecols=col_list
    ).rename(
        columns={"structure_exact_mass": "exact_mass"}
    ).drop_duplicates(

    )

    adducts = pandas.read_csv(
        filepath_or_buffer=paths["data"]["source"]["adducts"], sep='\t'
    ).transpose(

    )

    adducts.columns = adducts.iloc[0]

    adducts = adducts.filter(
        like='mass', axis=0)

    masses_adducts = pandas.concat(
        objs=[masses.reset_index(drop=True),
              adducts.reset_index(drop=True)],
        ignore_index=True,
        axis=1
    ).ffill(
        axis=0
    )

    masses_null = pandas.concat(
        objs=[pandas.DataFrame({'exact_mass': 0}, index=[0]).reset_index(drop=True),
              adducts.reset_index(drop=True)],
        ignore_index=True,
        axis=1
    ).ffill(
        axis=0
    )

    masses_adducts.columns = list(masses.columns.values) + list(adducts.columns.values)

    masses_null.columns = list(masses.columns.values) + list(adducts.columns.values)

    adducts_pos = form_adducts_pos(dataframe=masses_adducts, adducts=adducts).drop_duplicates()

    adducts_neg = form_adducts_neg(dataframe=masses_adducts, adducts=adducts).drop_duplicates()

    pure_pos = form_adducts_pos(dataframe=masses_null, adducts=adducts)

    pure_pos = pure_pos[pure_pos['adduct'].str.contains(pat="pos_1")]

    pure_neg = form_adducts_neg(dataframe=masses_null, adducts=adducts)

    pure_neg = pure_neg[pure_neg['adduct'].str.contains(pat="neg_1")]

    adducts_pos.to_csv(
        path_or_buf=os.path.join(
            paths["data"]["interim"]["adducts"]["path"],
            params["output"] +
            '_pos.tsv.gz'
        ),
        index=False
    )

    adducts_neg.to_csv(
        path_or_buf=os.path.join(
            paths["data"]["interim"]["adducts"]["path"],
            params["output"] +
            '_neg.tsv.gz'
        ),
        index=False
    )

    pure_pos.to_csv(
        path_or_buf=paths["data"]["interim"]["adducts"]["pos"],
        index=False
    )

    pure_neg.to_csv(
        path_or_buf=paths["data"]["interim"]["adducts"]["neg"],
        index=False
    )

    export_params(
        parameters=params,
        directory=paths["data"]["interim"]["config"]["path"],
        step=step)

else:
    print("""Sorry, your path does not match any file""")
