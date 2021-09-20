#!/usr/bin/env bash
# -*- coding: utf-8 -*-

if [ ! -d config ]; then
  echo "Sorry, you need to run that from where your config is."
  exit 1
fi


./src/get_lotus.sh &&
python src/prepare_lotus.py &&
python src/prepare_library.py &&
python src/prepare_adducts.py &&
./src/get_example_isdb.sh &&
./src/get_gnverifier.sh &&
python src/prepare_gnps.py &&
python src/prepare_isdb.py &&
python src/prepare_edges.py &&
python src/prepare_features_components.py &&
python src/prepare_features_classification.py &&
python src/prepare_taxa.py &&
# python src/process_annotations.py
