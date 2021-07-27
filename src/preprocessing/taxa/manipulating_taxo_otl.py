#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas


def manipulating_taxo_otl(dataframe):
    taxa_levels = [
        'input'
        'organismCleaned',
        'domain',
        'kingdom',
        'phylum',
        'class',
        'order',
        'infraorder',
        'family',
        'subfamily',
        'tribe',
        'subtribe',
        'genus',
        'subgenus',
        'species',
        'subspecies',
        'variety'
    ]

    df1 = dataframe[[
        'input',
        'organismCleaned',
        'organismCleaned_dbTaxoTaxonomy',
        'organismCleaned_dbTaxoTaxonRanks',
        'organismDbTaxo'
    ]].rename(
        columns={
            'organismCleaned_dbTaxoTaxonomy': 'name',
            'organismCleaned_dbTaxoTaxonRanks': 'ranks'
        }
    )

    df2 = df1[[
        'organismCleaned',
        'organismDbTaxo'
    ]]

    s_name = df1.name.str.split(pat='|', expand=True).join(df2).melt(id_vars=['organismCleaned', 'organismDbTaxo'],
                                                                     value_name='name')
    s_rank = df1.ranks.str.split(pat='|', expand=True).join(df2).melt(id_vars=['organismCleaned', 'organismDbTaxo'],
                                                                      value_name='rank').drop(
        columns=['organismCleaned', 'organismDbTaxo', 'variable'])

    df3 = pandas.concat([s_name.reset_index(drop=True), s_rank.reset_index(drop=True)], axis=1)

    df4 = df3[
        (df3['rank'] == 'domain') |
        (df3['rank'] == 'kingdom') |
        (df3['rank'] == 'phylum') |
        (df3['rank'] == 'class') |
        (df3['rank'] == 'order') |
        (df3['rank'] == 'infraorder') |
        (df3['rank'] == 'family') |
        (df3['rank'] == 'subfamily') |
        (df3['rank'] == 'tribe') |
        (df3['rank'] == 'subtribe') |
        (df3['rank'] == 'genus') |
        (df3['rank'] == 'subgenus') |
        (df3['rank'] == 'species') |
        (df3['rank'] == 'subspecies') |
        (df3['rank'] == 'variety')
        ][['organismCleaned', 'variable', 'name', 'rank']].reset_index(drop=True).drop_duplicates()

    df4 = df1[['input', 'organismCleaned']].merge(df4)

    df5 = df4.pivot(
        index=['input', 'organismCleaned', 'variable'],
        columns='rank',
        values='name'
    )

    df6 = df5.groupby(['input', 'organismCleaned']).fillna(
        method='bfill').fillna(
        method='ffill').unstack(
    ).droplevel(
        level=1,
        axis=1
    ).drop_duplicates()

    df7 = df6.loc[:, df6.columns.isin(taxa_levels)].reset_index(
    ).drop_duplicates()

    df8 = df7.loc[:, ~df7.columns.duplicated()]

    for i in taxa_levels:
        if i not in df8:
            df8[i] = None

    df9 = df8.rename(
        columns={
            'input': 'organismOriginal',
            'organismCleaned': 'organismCleaned',
            'domain': 'sample_organism_01_domain',
            'kingdom': 'sample_organism_02_kingdom',
            'phylum': 'sample_organism_03_phylum',
            'class': 'sample_organism_04_class',
            'order': 'sample_organism_05_order',
            'infraorder': 'sample_organism_05_1_infraorder',
            'tribe': 'sample_organism_07_tribe',
            'subtribe': 'sample_organism_07_1_subtribe',
            'genus': 'sample_organism_08_genus',
            'subgenus': 'sample_organism_08_1_subgenus',
            'species': 'sample_organism_09_species',
            'subspecies': 'sample_organism_09_1_subspecies',
            'variety': 'sample_organism_10_variety'}
    ).drop_duplicates()

    return (df9)
