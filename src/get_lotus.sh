#!/usr/bin/env bash
# -*- coding: utf-8 -*-

source parse_yaml.sh
source warning.sh

eval $(parse_yaml paths.yaml)

cd $base_dir

mkdir -p $data_source_libraries_path

wget "https://osf.io/rheq5/download" -O $data_source_libraries_lotus
