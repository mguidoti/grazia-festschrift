import pandas as pd
from os import path


def transform(filepath, filename):
  """

  Args:
      filepath (str): path where the input file is located
      filename (str): name of the input file
  """
  
  # Creating df, dealing with None
  df = pd.read_csv(path.join(filepath, filename))

  df['minted_dois'] = df.doi.apply(lambda x: 'zenodo' in x)
  
  df_minted = df.minted_dois.value_counts()
  
  df_minted.index.name = 'minted_dois'
  df_minted.rename('counts', inplace=True)
  
  df_minted.to_csv(path.join('output', '{}-minted_dois.csv'.format(
                                                                filename[:-4])),
                      index=True )
  
  