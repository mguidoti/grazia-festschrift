import pandas as pd
from os import path

# Creating custom wrangling method
def fix_names(x):
  """[summary]

  Args:
      x ([type]): [description]

  Returns:
      [type]: [description]
  """
  
  x = x.replace(',', '').replace('sp. nov.', ''
                       ).replace('abruptus (Walker', 'Walker'
                       ).replace('achilles Stal', 'Stal'
                       ).replace('acuminata Dallas', 'Dallas'
                       ).replace('amplus (Walker', 'Walker')

  if x[-1] == '.':
      x = x[:-1]

  return [x.strip() for x in x.split('&')]


def transform(filepath, filename):

  # Create pandas.DataFrame
  df = pd.read_csv(path.join(filepath, filename))

  # Filling NaNs
  df.fillna('None', inplace=True)

  # Control block: define transform and groupby column by the presence of
  # specific groupby columns
  transform_column = ''
  groupby_column = ''
  
  if 'Number of Treatment Citations' in df.columns:
    
    transform_column = 'Cited Authors'
    groupby_column = 'Number of Treatment Citations'
  
  elif 'Number of Materials Citations' in df.columns:
    
    transform_column = 'Collector Name'
    groupby_column = 'Number of Materials Citations'
  
  else:
    
    transform_column = 'Taxon Autority Name'
    groupby_column = 'Number of Treatments'
      
  # Apply the wrangling custom method to the target column
  df['Fixed'] = df[transform_column].apply(fix_names)

  # Explode rows with lists into separate rows
  df = df.apply(pd.Series.explode)

  # Get rid of accents
  df['Fixed'] = df['Fixed'].str.normalize('NFKD')\
        .str.encode('ascii', errors='ignore')\
        .str.decode('utf-8')   
    
  # Group by, providing the sum of treatments
  df_authors = df.groupby(['Fixed'])[[groupby_column, 'Fixed']
                                     ].sum().sort_values(
                                       by=[groupby_column], ascending=False)

  df_authors.to_csv(path.join('output', '{}-transformed.csv'.format(
                                                                filename[:-4])))