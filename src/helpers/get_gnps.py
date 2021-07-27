#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas


def read_features(gnps):
    path = 'http://gnps.ucsd.edu/ProteoSAFe/DownloadResultFile?task=' + gnps + '&block=main&file=quantification_table_reformatted/'

    file = pandas.read_csv(
        filepath_or_buffer=path
    )
    return file


def read_metadata(gnps):
    path = 'http://gnps.ucsd.edu/ProteoSAFe/DownloadResultFile?task=' + gnps + '&block=main&file=metadata_table/'

    file = pandas.read_csv(
        filepath_or_buffer=path,
        sep='\t'
    )
    return file


def read_results(gnps):
    path = 'http://gnps.ucsd.edu/ProteoSAFe/DownloadResultFile?task=' + gnps + '&block=main&file=DB_result/'

    file = pandas.read_csv(
        filepath_or_buffer=path,
        sep='\t'
    )
    return file


def read_clusters(gnps):
    path = 'http://gnps.ucsd.edu/ProteoSAFe/DownloadResultFile?task=' + gnps + '&block=main&file=clusterinfo_summary/'

    file = pandas.read_csv(
        filepath_or_buffer=path
    )
    return file


def read_nap(gnps):
    path = 'https://proteomics2.ucsd.edu/ProteoSAFe/DownloadResultFile?task=' + gnps + '&block=main&file=final_out/node_attributes_table.tsv'

    file = pandas.read_csv(
        filepath_or_buffer=path
    )
    return file


def read_edges(gnps):
    path = 'http://gnps.ucsd.edu/ProteoSAFe/DownloadResultFile?task=' + gnps + '&block=main&file=networkedges_selfloop/'

    file = pandas.read_csv(
        filepath_or_buffer=path,
        sep='\t'
    )
    return file
