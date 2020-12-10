import countries
import authors


if __name__ == "__main__":
  
  input_folder = 'input'

  coauthors_countries_file = 'grazia-festschrift-coauthors_data.csv'
  taxon_authority_file = 'grazia-festschrift-tb_stats-taxon_authority_names.csv'
  collectors_file = 'grazia-festschrift-tb_stats-collector_name.csv'
  treat_cit_authors_file = ('grazia-festschrift-tb_stats-treatCit_cited_authors'
                            '.csv')  

  # Starting transformation scripts
  countries.transform(input_folder, coauthors_countries_file)
  
  authors.transform(input_folder, taxon_authority_file)
  authors.transform(input_folder, collectors_file)
  authors.transform(input_folder, treat_cit_authors_file)