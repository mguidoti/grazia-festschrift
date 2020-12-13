import pandas as pd
from os import path


def fix_journal(entry):
  """[summary]

  Args:
      entry ([type]): [description]

  Returns:
      [type]: [description]
  """
  
  fixes = {
      'Zootaxa': [
          'Zootaxa (Auckland. Print)', 
          'Zootaxa (Online)'
          ],
      'Neotropical Entomology': [
          'NEOTROPICAL ENTOMOLOGY', 
          'Neotropical Entomology (Impresso)'
          ],
      'Revista Brasileira de Entomologia': [
          'Revista Brasileira de Entomologia (Impresso)'
          ],
      'Zoologia': [
          'Zoologia (Curitiba. Impresso)'
          ],
      'Acta Entomologica Musei Nationalis Pragae': [
          'Acta entomologica Musei Nationalis Pragae', 
          'ACTA ENTOMOLOGICA MUSEI NATIONALIS PRAGAE'
          ],
      'Revista Brasileira de Biociências': [
          'Revista Brasileira de Biociências (Online)'
          ],
      'Cytogenetic and Genome Research': [
          'Cytogenetic and Genome Research (Printed ed.)'
          ],
      'Cladistics': [
          'Cladistics (Westport)'
          ],
      'Entomologica Americana': [
          'Entomologica Americana (New York. Print)'
          ],
      'ZooKeys': [
          'ZooKeys (Online)'
          ],
      'Memórias do Instituto Oswaldo Cruz': [
          'Memórias do Instituto Oswaldo Cruz (Impresso)'
          ],
      'Zoomorphology': [
          'Zoomorphology (Berlin. Print)'
          ],
      'Biota Neotropica': [
          'Biota Neotropica (Edição em português. Impresso)',
          'Biota Neotropica (Online. Edição em Inglês)'
          ],
      'The Florida Entomologist': [
          'FLORIDA ENTOMOLOGIST'
          ],
      'Systematic Entomology': [
        'Systematic Entomology (Print)'
          ],
      'Brazilian Journal of Biology': [
        'BRAZILIAN JOURNAL OF BIOLOGY'
          ],
      'Beaufortia': [
        'Beaufortia (Amsterdam)'
          ],
      'Zoomorphology': [
        'ZOOMORPHOLOGY'
          ],
      'Zoologischer Anzeiger': [
        'ZOOLOGISCHER ANZEIGER'
          ],
      'Brazilian Journal of Biology': [
        'BRAZILIAN JOURNAL OF BIOLOGY (ONLINE)',
        'BRAZILIAN JOURNAL OF BIOLOGY'
          ],
      'Environmental Entomology': [
        'ENVIRONMENTAL ENTOMOLOGY'
          ]
    }

  for key, value in fixes.items():
      if entry in value:
          return key
      
  return entry


def fix_pagination(entry):
  
  pages = entry.split('-')
  start_page = int(pages[0])
  
  if len(pages) > 1:
    end_page = int(pages[1])
    return end_page - start_page

  return 1


def transform(filepath, filename):
  """

  Args:
      filepath (str): path where the input file is located
      filename (str): name of the input file
  """
  
  # Creating df, dealing with None
  df = pd.read_csv(path.join(filepath, filename))

  df.Journal = df.Journal.apply(fix_journal)
  df['pages'] = df.Pagination.apply(fix_pagination)
  
  df.to_csv(path.join('output', '{}-transformed.csv'.format(
                                                      filename[:-4])),
            index=False )