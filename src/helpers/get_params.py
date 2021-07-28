#!/usr/bin/env python
# -*- coding: utf-8 -*-

from helpers.parse_cli_params import parse_cli_params
from helpers.parse_yaml_params import parse_yaml_params


def get_params(step, cli):
    params = parse_yaml_params(step)
    params = parse_cli_params(params, cli)
    return (params)
