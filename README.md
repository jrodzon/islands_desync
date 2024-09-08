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
