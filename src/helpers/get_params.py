#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .parse_cli_params import parse_cli_params
from .parse_yaml_params import parse_yaml_params


def get_params(step, cli):
    print('Loading parameters')
    params = parse_yaml_params(step)
    params = parse_cli_params(params, cli)
    return (params)
