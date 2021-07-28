#!/usr/bin/env bash

if [ ! -d config ]; then
  echo "Sorry, you need to run that from where your config is."
  exit 1
fi


./src/get_lotus.sh && python src/prepare_lotus.py &&
python src/prepare_library.py &&
python src/prepare_adducts.py