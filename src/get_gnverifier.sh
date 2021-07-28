#!/usr/bin/env bash
# -*- coding: utf-8 -*-

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
source "$SCRIPT_DIR"/get_platform.sh
source "$SCRIPT_DIR"/parse_yaml.sh
source "$SCRIPT_DIR"/warning.sh

eval $(parse_yaml paths.yaml)
cd $base_dir
eval $(parse_yaml config/versions.yaml)

mkdir -p $bin_path
wget -O - https://github.com/gnames/gnverifier/releases/download/$gnverifier/gnverifier-$gnverifier-$OS.tar.gz | tar xOz gnverifier >bin/gnverifier
chmod +x bin/gnverifier
