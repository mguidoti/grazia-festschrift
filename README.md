<h2 align="center">
  Grazia Festschrift Wrangling Scripts
</h2>

<p align="center">
  <a href="https://doi.org/10.5281/zenodo.4313975">
      <img alt="Digital Object Identifier" scr="https://img.shields.io/badge/DOI-10.5281%2Fzenodo.4313975-blue"/>
  </a>
</p>

This is a dedicated repository to the wrangling scripts used to prepare Guidoti's at al. contribution to Zootaxa's special issue to honor Jocelia Grazia, a Brazilian entomologist with an active and fruitful carreer of over 50 years.

## Running

Install Pipenv, and run pipenv install. Next, please, download the used dataset first. Then, place the following files in a knonw folder:

- grazia-festschrift-coauthors_data.csv
- grazia-festschrift-tb_stats-collector_name.csv
- grazia-festschrift-tb_stats-taxon_authority_names.csv
- grazia-festschrift-tb_stats-treatCit_cited_authors.csv

Edit main.py to indicate the path to this folder. Finally, navigate to this aforementioned folder using your terminal of preference and run `pipenv run python main.py`.

## License

MIT. For more detail, please access [here](https://github.com/mguidoti/grazia-festschrift/blob/main/LICENSE).
