#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

import yaml


def parse_yaml_params(step):
    with open("config/default/" + step + ".yaml", 'r') as stream:
        try:
                params = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
                print(exc)
    with open("config/params/" + step + ".yaml", 'r') as stream:
        try:
                params = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
                print(exc)
    return params
