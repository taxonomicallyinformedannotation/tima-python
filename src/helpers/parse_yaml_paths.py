#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

import yaml


def parse_yaml_paths():
    print('Loading paths')
    with open("paths.yaml", 'r') as stream:
        try:
            paths = yaml.safe_load(stream)
            os.chdir(paths["base_dir"])
        except yaml.YAMLError as exc:
            print(exc)
    return paths
