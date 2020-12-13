import pandas as pd
from os import path


def transform(filepath, filename):
  """

  Args:
      filepath (str): path where the input file is located
      filename (str): name of the input file
  """
  
  df = pd.read_csv(path.join(filepath, filename))
  
  df.fillna('other', inplace=True)
  #df.index.name = 'minted_dois'
  
  
  df.to_csv(path.join('output', '{}-transformed.csv'.format(
                                                                filename[:-4])),
                      index=False )