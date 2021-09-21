#!/usr/bin/env bash

if [ ! -d config ]; then
  echo "Sorry, you need to run that from where your config is."
  exit 1
fi


bash src/get_lotus.sh &&
conda run -n tima-python python src/prepare_lotus.py &&
conda run -n tima-python python src/prepare_library.py &&
conda run -n tima-python python src/prepare_adducts.py &&
bash src/get_example_isdb.sh &&
bash src/get_gnverifier.sh &&
conda run -n tima-python python src/prepare_gnps.py &&
conda run -n tima-python python src/prepare_isdb.py &&
conda run -n tima-python python src/prepare_edges.py &&
conda run -n tima-python python src/prepare_features_components.py &&
conda run -n tima-python python src/prepare_features_classification.py &&
conda run -n tima-python python src/prepare_taxa.py # &&
# conda run -n tima-python python src/process_annotations.py
