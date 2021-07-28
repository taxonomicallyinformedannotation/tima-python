## Repo preparation

### To run in docker:

```shell
docker build -t tima-python . # optional
docker run -it --rm -v $PWD:/app tima-python
```

### To run locally:

```shell
conda env create -f environment.yml &&
conda activate tima-python
```

## Structure-organism pairs library

```shell
./src/get_lotus.sh && 
python src/prepare_lotus.py &&
# python prepare_dnp.py && # only if you have access to it
python src/prepare_library.py &&
python src/prepare_adducts.py &&
```

## Annotations

### Get MS2 annotations

```shell
# normally it would be 'python src/process_spectra.py' but for now we have to think about it.
# instead we provide an example file coming from the new ISDB.
# It also works with annotations coming from GNPS (see next steps)
./src/get_example_isdb.sh
```

### Format MS2 annotations

```shell
# depending on the annotation tool you used
python src/prepare_gnps.py && # optional 
python src/prepare_isdb.py
```

### Complement MS2 annotations (with spectral clusters and chemical taxonomy of annotations)

```shell
python src/prepare_edges.py &&
python src/prepare_features_components.py &&
python src/prepare_features_classification.py 
```

### Get biological taxonomy information

```shell
./src/get_gnverifier.sh && 
python src/prepare_taxa.py
```

## And finally the graal!

### NOT READY YET

```shell
# python process_annotations.py
```

NOTE: you can use --help or -h argument for all .py steps to get more info
