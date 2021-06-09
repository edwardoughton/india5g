5G Assessment for India (India5G)
====
[![Build Status](https://travis-ci.com/edwardoughton/india5g.svg?branch=master)](https://travis-ci.com/edwardoughton/india5g)
[![Coverage Status](https://coveralls.io/repos/github/edwardoughton/India5G/badge.svg)](https://coveralls.io/github/edwardoughton/India5G?branch=master)

This codebase enables 5G strategies to be tested with the ultimate aim of
helping to connect more people to a faster internet, as applied here for India.

Importantly, we provide all data inputs and code so that the results can be reproduced. Both
unit tests and integration tests are provided for the codebase to ensure reliability.

Using conda
==========

The recommended installation method is to use conda, which handles packages and virtual
environments, along with the conda-forge channel which has a host of pre-built libraries and
packages.

Create a conda environment called `India5G`:

    conda create --name india5g python=3.6 gdal geopandas

Activate it (run this each time you switch projects):

    conda activate india5g

Install `India5G`:

    python setup.py install

Alternatively, for development purposes, clone this repo and run:

    python setup.py develop


Download necessary data
=======================

You will need numerous input data sets.

First, download the Global Administrative Database (GADM), following the link below and making
sure you download the "six separate layers.":

- https://gadm.org/download_world.html

Place the data into the following path `data/raw/gadm36_levels_shp`.

Then download the WorldPop global settlement data from:

- https://www.worldpop.org/geodata/summary?id=24777.

Place the data in `data/raw/settlement_layer`.

Next, download the nightlight data here:

https://ngdc.noaa.gov/eog/data/web_data/v4composites/F182013.v4.tar

Place the unzipped data in `data/raw/nightlights/2013`.

Obtain the Mobile Coverage Explorer data from Collins Bartholomew:

https://www.collinsbartholomew.com/mobile-coverage-maps/mobile-coverage-explorer/

Place the data into `data/raw/Mobile Coverage Explorer`.

Once complete, run the following to preprocess all data:

    python scripts/preprocess.py


Using the model
===============

To obtain model results once all inputs have been generated, simply execute the runner script:

    python scripts/run.py


Thanks for the support
======================

**India5G** was written and developed at George Mason University.
