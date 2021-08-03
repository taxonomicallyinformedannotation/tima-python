#!/usr/bin/env bash
# -*- coding: utf-8 -*-

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
source "$SCRIPT_DIR/"parse_yaml.sh
source "$SCRIPT_DIR/"warning.sh

eval $(parse_yaml paths.yaml)
cd $base_dir || exit
mkdir -p $data_interim_path
mkdir -p $data_interim_annotations_path

wget "https://metabo-store.nprod.net/tima_example_files/interim/example_isdb_result.tsv.gz" -O data/interim/annotations/example_isdb_result.tsv.gz
