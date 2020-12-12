import pandas as pd
from os import path

from authors import fix_names


def transform(filepath, filename):
  """

  Args:
      filepath (str): path where the input file is located
      filename (str): name of the input file
  """
  
  # Creating df, dealing with None
  df = pd.read_csv(path.join(filepath, filename))

  df.fillna('None', inplace=True)

  # Getting countries without Grazia, adding to a list
  coauthors_1 = df[~df['Author 1'].str.contains('Grazia')]['Author 1']
  coauthors_2 = df[~df['Author 2'].str.contains('Grazia')]['Author 2']
  coauthors_3 = df[~df['Author 3'].str.contains('Grazia')]['Author 3']
  coauthors_4 = df[~df['Author 4'].str.contains('Grazia')]['Author 4']
  coauthors_5 = df[~df['Author 5'].str.contains('Grazia')]['Author 5']
  coauthors_6 = df[~df['Author 6'].str.contains('Grazia')]['Author 6']
  coauthors_7 = df[~df['Author 7'].str.contains('Grazia')]['Author 7']

  coauthors = []

  coauthors += coauthors_1.to_list()
  coauthors += coauthors_2.to_list()
  coauthors += coauthors_3.to_list()
  coauthors += coauthors_4.to_list()
  coauthors += coauthors_5.to_list()
  coauthors += coauthors_6.to_list()
  coauthors += coauthors_7.to_list()

  # Filtering None out, transforming in pandas.Series to get frequency counts
  coauthors = [country for country in coauthors if country != 'None']

  coauthors = pd.Series(coauthors)
  
  coauthors.apply(fix_names)
  
  coauthors = coauthors.value_counts()
  
  coauthors.rename('counts', inplace=True)
  coauthors.index.name = 'coauthors'
  
  coauthors.to_csv(path.join('output', '{}-names-transformed.csv'.format(
                                                                filename[:-4])),
                      index=True )
  
  