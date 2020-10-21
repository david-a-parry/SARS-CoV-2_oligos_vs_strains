# SARS-CoV-2_oligos_vs_strains

Analysis of oligo vs SARS-COV2 strain sequences

Code is provided as a [jupyter-notebook](https://jupyter.org/)

## Requirements

You will need to have jupyter-lab or jupyter-notebook [installed](https://jupyter.org/install.html). Python3 is also required, but should be installed if you have jupyter up and running.

Python modules required:

* biopython
* pandas
* numpy
* seaborn

## How to run

First clone this repository

~~~

git clone https://github.com/david-a-parry/SARS-CoV-2_oligos_vs_strains.git

cd SARS-CoV-2_oligos_vs_strains

~~~

You will need to register with GISAID in order to obtain sequence and multiple alignment data for SARS-COV-2 strains from their EpiCov database. Required files are the:

* nextfasta file (sequences_2020-10-12_07-17.fasta.gz)
* msa_1021 file (msa_1012.tar.xz)

Download these files to the SARS-CoV-2_oligos_vs_strains directory created when you cloned this repository. Next, extract the multiple alignment file from the msa_1012.tar.xz archive and run the reheader_msa.py script to reformat headers and remove duplicate sequence IDs (strains sequenced more than once).

~~~
tar xvf msa_1012.tar.xz
python3 reheader_msa.py  msa_1012.fasta
~~~

If these steps completed successfully you are ready to run the code in the provided 'primer variant counts' notebook. From the SARS-CoV-2_oligos_vs_strains run `jupyter-notebook`.
