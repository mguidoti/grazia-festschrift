import pandas as pd
import numpy as np

import os


# File and file path
filepath = 'C:/Users/poa/Desktop/grazia/datasets_to_Zenodo'
coauthors_file = 'grazia-festschrift-coauthors_data.csv'


# Creating df, dealing with None
df_coauthors = pd.read_csv(os.path.join('input', coauthors_file))

df_coauthors.fillna('None', inplace=True)


# Getting countries without Grazia, adding to a list
countries_1 = df_coauthors[~df_coauthors['Author 1'].str.contains('Grazia')]['Author 1 Country']
countries_2 = df_coauthors[~df_coauthors['Author 2'].str.contains('Grazia')]['Author 2 Country']
countries_3 = df_coauthors[~df_coauthors['Author 3'].str.contains('Grazia')]['Author 3 Country']
countries_4 = df_coauthors[~df_coauthors['Author 4'].str.contains('Grazia')]['Author 4 Country']
countries_5 = df_coauthors[~df_coauthors['Author 5'].str.contains('Grazia')]['Author 5 Country']
countries_6 = df_coauthors[~df_coauthors['Author 6'].str.contains('Grazia')]['Author 6 Country']
countries_7 = df_coauthors[~df_coauthors['Author 7'].str.contains('Grazia')]['Author 7 Country']

countries = []

countries += countries_1.to_list()
countries += countries_2.to_list()
countries += countries_3.to_list()
countries += countries_4.to_list()
countries += countries_5.to_list()
countries += countries_6.to_list()
countries += countries_7.to_list()


# Filtering None out, transforming in pandas.Series to get frequency counts
countries = [country for country in countries if country != 'None']

countries = pd.Series(countries)


# Transforming back into a pandas.DataFrame to easily rename columns
df_countries = countries.value_counts().rename_axis('countries').reset_index(name='counts')

df_countries.to_csv(os.path.join('output', 'grazia-festschrift-coauthors_data.csv'))
