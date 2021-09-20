# Taxonomically Informed Metabolite Annotation

The initial work is available at https://doi.org/10.3389/fpls.2019.01329, and many improvements have been made since
then. 
The worklow is illustrated in Figure 1.

![Figure 1](./img/tima.svg)

This repository contains everything needed to perform **T**axonomically **I**nformed **M**etabolite **A**nnotation.

It is provided with an example from well-known pharmacopoeia plants.

Here is what you *minimally* need:

- A feature list with *or without* candidate annotations, if you are using GNPS, it can be your GNPS job ID.
- The source organism of the extract you are annotating, if you are associating metadata within GNPS, it can be your
  GNPS job ID.
- An edge list, if you are using GNPS, it can be your GNPS job ID.

Optionally, you may want to add:

- An in-house structure-organism pairs library (we provide **LOTUS** as starting point for each user)
- Your own manual or automated annotations (we currently support annotations coming from ISDB and SIRIUS)

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
bash src/get_lotus.sh && 
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
bash src/get_example_isdb.sh
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
bash src/get_gnverifier.sh && 
python src/prepare_taxa.py
```

## And finally the graal!

### NOT READY YET

```shell
# python process_annotations.py
```

NOTE: you can use --help or -h argument for all .py steps to get more info
