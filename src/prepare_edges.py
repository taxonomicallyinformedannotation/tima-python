#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This script prepares edges"""

from helpers.get_gnps import read_edges
from helpers.parse_yaml_params import parse_yaml_params
from helpers.parse_yaml_paths import parse_yaml_paths

paths = parse_yaml_paths()

params = parse_yaml_params(step="prepare_edges")

## TODO manual possibility to add

if params["tool"] == 'gnps':
    edges_table = read_edges(gnps=params["gnps"])

    edges_table_treated = edges_table.rename(
        columns={
            params["source_name"]: 'feature_source',
            params["target_name"]: 'feature_target'
        }
    )[['feature_source', 'feature_target']].query(
        'feature_source != feature_target'
    )

    edges_table_treated.to_csv(
        path_or_buf=params["output"],
        index=False
    )
else:
    print("""manual version still to do, Sorry""")

## TODO export params when modified with CLI
