#!/usr/bin/env bash
# -*- coding: utf-8 -*-

source get_platform.sh
source parse_yaml.sh
source warning.sh

eval $(parse_yaml paths.yaml)
cd $base_dir
eval $(parse_yaml config/versions.yaml)

mkdir -p $bin_path
wget -o - https://github.com/gnames/gnverifier/releases/download/$gnverifier/gnverifier-$gnverifier-$OS.tar.gz | tar xOz gnverifier >bin/gnverifier
chmod +x bin/gnverifier
