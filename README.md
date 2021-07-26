## tl;dr:

```
## repo preparation

# NOT READY YET
# docker build -t tima . ## optional
# docker run -it --rm -v $PWD:/app tima bash ## optional
# conda env create -f environment.yml &&
# conda activate tima &&


## get a working structure-organism pairs library

bash src/get-lotus.sh &&
cd src &&
python prepare_lotus.R &&
## python prepare_dnp.R && ## only if you have access to it
python prepare_library.R &&
python prepare_adducts.R &&


## get spectral matches
### (did not copy it there, see how we manage this)
cd .. &&
bash src/get_example_isdb.sh && ## get an example result from new isdb without python


## prepare all files for weighting

# NOT READY YET
bash src/get_gnverifier.sh &&
cd src &&
# python prepare_gnps.R && ## optional
# python prepare_isdb.R &&
# python prepare_features_components.R &&
# python prepare_features_classification.R &&
python prepare_edges.R && 
# python prepare_taxa.R 

## And finally the graal!
# NOT READY YET
#python process_annotations.R

# NOT READY YET
## you can use --help or -h argument for all .py steps to get more info
```