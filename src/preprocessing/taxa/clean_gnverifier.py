#!/usr/bin/env python
# -*- coding: utf-8 -*-

from preprocessing.taxa.preclean_gnverifier import preclean_gnverifier


def clean_gnverifier(file):
    dataOrganismVerified = preclean_gnverifier(file).iloc[1:, :]

    df1 = dataOrganismVerified[dataOrganismVerified.input.notnull()]

    df1 = df1.assign(col=[organismCleaned if organismDbTaxo == 'Open Tree of Life' else '' for organismDbTaxo in
                          df1['organismCleaned']]).rename(
        columns={
            'input': 'organism'
        }
    )

    df2 = df1[['organism', 'organismCleaned']].drop_duplicates()

    df2['count'] = df2.groupby('organism')['organism'].transform('count')

    warning = df2[df2['count'] == 1][df2['organismCleaned'].isnull()]

    if len(warning.index) != 0:
        print('Warning: ' + warning["organism"] + ' has no translation, trying with a more flexible solution')

        organism_table_2 = dataOrganismVerified[['input', 'organismCleaned']].drop_duplicates()
        organism_table_2 = \
        organism_table_2[organism_table_2['input'] != organism_table_2['organismCleaned']][['organismCleaned']][
            organism_table_2['organismCleaned'].notnull()].drop_duplicates()

        if len(organism_table_2.index) != 0:

            organism_table_2.to_csv(
                path_or_buf=paths["data"]["interim"]["taxa"]["original_2"],
                index=False
            )

            print('Submitting to GNVerifier')

            os.system(
                'bash' + " " + paths["src"]["gnverifier"]
            )

            dataOrganismVerified_2 = preclean_gnverifier(file).iloc[1:, :].rename(
                columns={
                    'input': 'organism'
                }
            )

            dataOrganismVerified_3 = pandas.concat([dataOrganismVerified, dataOrganismVerified_2])

            dataOrganismVerified_3 = dataOrganismVerified_3[
                dataOrganismVerified_3['organismDbTaxo'] == 'Open Tree of Life'].drop_duplicates()

            warning_2 = organism_table.join(dataOrganismVerified_3)

            warning_2 = warning_2[warning_2['organism'].notnull()][warning_2['organismDbTaxo'].isnull()]

            if len(organism_table_2.index) != 0:
                print('Warning: ' + warning_2["organism"] + ' has no translation')
                print('Check at https://tree.opentreeoflife.org/')

            else:
                print('Good news, all your organisms were found!')

        else:
            dataOrganismVerified_3 = dataOrganismVerified[
                dataOrganismVerified['organismDbTaxo'] == 'Open Tree of Life'].drop_duplicates()
            print('We will not find more!')

    else:
        dataOrganismVerified_3 = dataOrganismVerified[
            dataOrganismVerified['organismDbTaxo'] == 'Open Tree of Life'].drop_duplicates()
        print('Good news, all your organisms were found!')

    return (dataOrganismVerified_3)
