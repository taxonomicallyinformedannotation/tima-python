#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from time import strftime

import yaml


def export_params(parameters, directory, step):
    print('path to used parameters is ' + directory)

    filename = os.path.join(directory, strftime("%Y%m%d_%H%M%S") + '_' + step + '.yaml')

    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(filename, 'w') as file:
        documents = yaml.dump(parameters, file)
