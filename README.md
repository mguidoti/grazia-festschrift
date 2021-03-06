<h2 align="center">
  Guidoti <em>et al.</em>'s Grazia Festschrift Wrangling Scripts
</h2>

<p align="center">
  <a href="https://doi.org/10.5281/zenodo.4319340">
      <img alt="Digital Object Identifier" src="https://zenodo.org/badge/DOI/10.5281/zenodo.4319340.svg"/>
  </a>
</p>

This is a dedicated repository to the wrangling scripts used to prepare Guidoti's et al. contribution to Zootaxa's special issue to honor Jocelia Grazia, a Brazilian entomologist with an active and fruitful career of over 50 years.

## Running

Install [Pipenv](https://pypi.org/project/pipenv/), and `run pipenv install`. Next, please, download the [used dataset](http://zenodo.org/record/4319233) first. Then, place the following files in a knonw folder:

- grazia-festschrift-basic_metadata.csv
- grazia-festschrift-coauthors_data.csv
- grazia-festschrift-tb_stats-collector_name.csv
- grazia-festschrift-tb_stats-taxon_authority_names.csv
- grazia-festschrift-tb_stats-taxonomic_ranks.csv
- grazia-festschrift-tb_stats-taxonomic_status.csv
- grazia-festschrift-tb_stats-treatCit_cited_authors.csv

Edit main.py to indicate the path to this folder. Finally, navigate to the aforementioned folder using your terminal of preference and run `pipenv run python main.py`.

## License

MIT. For more detail, please access [here](https://github.com/mguidoti/grazia-festschrift/blob/main/LICENSE).
