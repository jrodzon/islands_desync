# Islands desync
This repository contains genetic algorithm with island version, where migrations may be desynchronised.

## Preparing anaconda environment
You can create conda environment with the following commands:
```shell
conda env create --file environment.yml
conda activate islands_desync
pip install jmetalpy
```
> Since `jmetalpy` is not available via conda, we have to use `pip` for this task.

## Running locally
There is a designated script to run the project locally:
```shell
./local_run.sh
```

## LABS Problem
The LABS problem is a common calculation problem, which is really hard to solve for longer sequences (exponential complexity).
Here is a nice publication that describes this problem with its applications:
[Low autocorrelation binary sequences](https://www-e.ovgu.de/mertens/pubs/labs-16.pdf)

The experiment results are in [the jupyter notebook](experiments_interpretations/LABS/results.ipynb).
