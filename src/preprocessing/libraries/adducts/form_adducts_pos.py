#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This script prepares adducts from the \n,
   structure-organism pairs for further processing"""

import pandas


def form_adducts_pos(dataframe, adducts):
    dataframe_pos = dataframe.assign(
        pos_3_3proton=(dataframe['exact_mass'] +
                       3 * dataframe['proton']) / 3,
        pos_3_2proton1sodium=(dataframe['exact_mass'] +
                              2 * dataframe['proton'] +
                              dataframe[
                                  'sodium']) / 3,
        pos_3_1proton2sodium=(dataframe['exact_mass'] +
                              dataframe['proton'] +
                              2 * dataframe[
                                  'sodium']) / 3,
        pos_3_3sodium=(dataframe['exact_mass'] +
                       3 * dataframe['sodium']) / 3,
        pos_2_2proton=(dataframe['exact_mass'] +
                       2 * dataframe['proton']) / 2,
        pos_2_2proton1ammonium=
        (dataframe['exact_mass'] +
         2 * dataframe['proton'] +
         dataframe['ammonium']) / 2,
        pos_2_1proton1sodium=(dataframe['exact_mass'] +
                              dataframe['proton'] +
                              dataframe['sodium']) / 2,
        pos_2_1proton1potassium=(
                                        dataframe['exact_mass'] +
                                        dataframe['proton'] +
                                        dataframe['potassium']) / 2,
        pos_2_2proton1acetonitrile=(
                                           dataframe['exact_mass'] +
                                           2 * dataframe['proton'] +
                                           dataframe['acetonitrile']) / 2,
        pos_2_2sodium=(dataframe['exact_mass'] +
                       2 * dataframe['sodium']) / 2,
        pos_2_2proton2acetonitrile=(dataframe['exact_mass'] +
                                    2 * dataframe['proton'] +
                                    2 * dataframe[
                                        'acetonitrile']) / 2,
        pos_2_2proton3acetonitrile=(dataframe['exact_mass'] +
                                    2 * dataframe['proton'] +
                                    3 * dataframe[
                                        'acetonitrile']) / 2,
        # pos_1_minus2water1proton = dataframe['exact_mass'] - 2 * dataframe['water'] + dataframe['proton'],
        # pos_1_minus1water1proton = dataframe['exact_mass'] - dataframe['water'] + dataframe['proton'],
        pos_1_1proton=dataframe['exact_mass'] +
                      dataframe['proton'],
        # pos_1_minus1water1sodium=dataframe['exact_mass'] - dataframe['water'] + dataframe['sodium'],
        pos_1_1proton1ammonium=dataframe['exact_mass'] +
                               dataframe['proton'] +
                               dataframe['ammonium'],
        pos_1_sodium=dataframe['exact_mass'] +
                     dataframe['sodium'],
        pos_1_1proton1methanol=dataframe['exact_mass'] +
                               dataframe['proton'] +
                               dataframe['methanol'],
        pos_1_1potassium=dataframe['exact_mass'] +
                         dataframe['potassium'],
        pos_1_1proton1acetonitrile=dataframe['exact_mass'] +
                                   dataframe['proton'] +
                                   dataframe[
                                       'acetonitrile'],
        pos_1_minus1proton2sodium=dataframe['exact_mass'] -
                                  dataframe['proton'] +
                                  2 * dataframe[
                                      'sodium'],
        pos_1_1proton1ethylamine=dataframe['exact_mass'] +
                                 dataframe['proton'] +
                                 dataframe['ethylamine'],
        pos_1_1proton1isopropanol=dataframe['exact_mass'] +
                                  dataframe['proton'] +
                                  dataframe[
                                      'isopropanol'],
        pos_1_1sodium1acetonitrile=dataframe['exact_mass'] +
                                   dataframe['sodium'] +
                                   dataframe[
                                       'acetonitrile'],
        pos_1_minus1proton2potassium=dataframe['exact_mass'] -
                                     dataframe['proton'] +
                                     2 * dataframe[
                                         'potassium'],
        pos_1_1proton1dmso=dataframe['exact_mass'] +
                           dataframe['proton'] +
                           dataframe['dmso'],
        pos_1_1proton2acetonitrile=dataframe['exact_mass'] +
                                   dataframe['proton'] +
                                   2 * dataframe[
                                       'acetonitrile'],
        # pos_IsoPNa-H = dataframe['exact_mass'] - dataframe['proton'] + dataframe['isopropanol'] + dataframe['sodium)
        pos_2MH=2 * dataframe['exact_mass'] +
                dataframe['proton'],
        pos_2MHNH3=2 * dataframe['exact_mass'] +
                   dataframe['proton'] +
                   dataframe['ammonium'],
        pos_2MNa=2 * dataframe['exact_mass'] +
                 dataframe['sodium'],
        pos_2MK=2 * dataframe['exact_mass'] +
                dataframe['potassium'],
        pos_2MHCH3CN=2 * dataframe['exact_mass'] +
                     dataframe['proton'] +
                     dataframe['acetonitrile'],
        pos_2MCH3CNNa=2 * dataframe['exact_mass'] +
                      dataframe['acetonitrile'] +
                      dataframe['sodium']
    ).drop(
        list(adducts.columns.values),
        axis=1
    )

    dataframe_pos = pandas.melt(
        dataframe_pos,
        id_vars=['exact_mass'],
        value_vars=list(dataframe_pos.columns.values)[1:],
        var_name='adduct',
        value_name='adduct_mass')
    return dataframe_pos
