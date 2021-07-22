#!/usr/bin/env bash
# -*- coding: utf-8 -*-

if [ ! -f LICENSE ]; then
  echo "Sorry, you need to run that from the root of the project."
  exit 1
fi

mkdir -p data/source/libraries
wget "https://osf.io/rheq5/download" -O data/source/libraries/lotus.csv.gz
