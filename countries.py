import pandas as pd
from os import path


def transform(filepath, filename):
  """Transform the input dataframe, unifying all authors columns after removing
  the lines of Grazia, to generate an unique frequency count based on co-authors
  only.

  Args:
      filepath (str): path where the input file is located
      filename (str): name of the input file
  """
  
  # Creating df, dealing with None
  df = pd.read_csv(path.join(filepath, filename))

  df.fillna('None', inplace=True)

  # Getting countries without Grazia, adding to a list
  countries_1 = df[~df['Author 1'].str.contains('Grazia')]['Author 1 Country']
  countries_2 = df[~df['Author 2'].str.contains('Grazia')]['Author 2 Country']
  countries_3 = df[~df['Author 3'].str.contains('Grazia')]['Author 3 Country']
  countries_4 = df[~df['Author 4'].str.contains('Grazia')]['Author 4 Country']
  countries_5 = df[~df['Author 5'].str.contains('Grazia')]['Author 5 Country']
  countries_6 = df[~df['Author 6'].str.contains('Grazia')]['Author 6 Country']
  countries_7 = df[~df['Author 7'].str.contains('Grazia')]['Author 7 Country']

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
  df_countries = countries.value_counts().rename_axis('countries'
                                                    ).reset_index(name='counts')

  # Saving to a new csv
  df_countries.to_csv(path.join('output', '{}-transformed.csv'.format(
                                                                filename[:-4])),
                      index=False )
