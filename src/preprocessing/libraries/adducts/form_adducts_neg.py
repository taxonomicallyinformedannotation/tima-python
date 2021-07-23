#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This script prepares adducts from the \n,
   structure-organism pairs for further processing"""

import pandas

def form_adducts_neg(dataframe, adducts):
    dataframe_neg = dataframe.assign(
        neg_3_3proton=(dataframe['exact_mass'] -
                       3 * dataframe['proton']) / 3,
        neg_2_2proton=(dataframe['exact_mass'] -
                       2 * dataframe['proton']) / 2,
        # neg_1_minus2waterminus1proton = dataframe['exact_mass'] - 2 * dataframe['water'] + dataframe['proton'],
        # neg_1_minus1waterminus1proton = dataframe['exact_mass'] - 2 * dataframe['water'] + dataframe['proton'],
        neg_1_minus1proton=dataframe['exact_mass'] -
                           dataframe['proton'],
        neg_1_minus2proton1sodium=(dataframe['exact_mass'] -
                                   2 * dataframe['proton'] +
                                   dataframe['sodium']),
        neg_1_1chlorine=dataframe['exact_mass'] +
                        dataframe['chlorine'],
        neg_1_minus2proton1potassium=
        dataframe['exact_mass'] -
        2 * dataframe['proton'] +
        dataframe['potassium'],
        neg_1_minus1proton1formic=dataframe['exact_mass'] -
                                  dataframe['proton'] +
                                  dataframe['formic'],
        neg_1_minus1proton1acetic=dataframe['exact_mass'] -
                                  dataframe['proton'] +
                                  dataframe['acetic'],
        neg_1_minus2proton1sodium1formic=dataframe['exact_mass'] -
                                         2 * dataframe['proton'] +
                                         dataframe['sodium'] +
                                         dataframe['formic'],
        neg_1_1bromine=(dataframe['exact_mass'] +
                        dataframe['bromine']),
        neg_1_minus1proton1tfa=(dataframe['exact_mass'] -
                                dataframe['proton'] +
                                dataframe[
                                    'tfa']),
        neg_2MH=2 * dataframe['exact_mass'] -
                dataframe['proton'],
        neg_2MFAH=2 * dataframe['exact_mass'] -
                  dataframe['proton'] +
                  dataframe['formic'],
        neg_2MACH=2 * dataframe['exact_mass'] -
                  dataframe['proton'] +
                  dataframe['acetic'],
        neg_3MH=3 * dataframe['exact_mass'] -
                dataframe['proton']
    ).drop(
        list(adducts.columns.values),
        axis=1
    )
    dataframe_neg = pandas.melt(
        dataframe_neg,
        id_vars=['exact_mass'],
        value_vars=list(dataframe_neg.columns.values)[1:],
        var_name='adduct',
        value_name='adduct_mass')
    return dataframe_neg