# Machine Learning in Bioinformatics: GeoGenome

This is the repository for an [article on Medium](https://burgshrimps.medium.com/machine-learning-in-bioinformatics-genome-geography-d1b1dbbfb4c2). The main idea is to build a machine learning model which can predict the geographical origin of an individual based on their genomic variation.
The main analysis is located in the Jupyter notebook "geogenome.ipynb". A really basic exemplary preprocessing analysis of NGS data for one sample can be found in "preprocess.sh"

## Hint
The calculation of the Hamming distances between all samples is quite computationally intensive. In case you don't want to redo the whole analysis you can skip that part and use the "samples_subset.tsv" and "ham_dist.txt" files.
