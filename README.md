## tl;dr:

```
# repo preparation

To run in docker:

```shell
docker build -t tima-python . # optional
docker run -it --rm -v $PWD:/app tima-python
```

To run locally:
```shell
conda env create -f environment.yml &&
conda activate tima-python
```


# get a working structure-organism pairs library

```shell
cd src
./get_lotus.sh && python prepare_lotus.py &&
# python prepare_dnp.py && # only if you have access to it
python prepare_library.py &&
python prepare_adducts.py &&

```
# get spectral matches
# (did not copy it there, see how we manage this)
cd .. &&
bash src/get_example_isdb.sh && # get an example result from new isdb without python


# prepare all files for weighting

# NOT READY YET
bash src/get_gnverifier.sh &&
cd src &&
python prepare_gnps.py && # optional
python prepare_isdb.py &&
# python prepare_features_components.py &&
# python prepare_features_classification.py &&
python prepare_edges.py && 
python prepare_taxa.py 

# And finally the graal!
# NOT READY YET
# python process_annotations.py

# NOTE: you can use --help or -h argument for all .py steps to get more info
```