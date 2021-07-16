5G Assessment for India (India5G)
====
[![Build Status](https://travis-ci.com/edwardoughton/india5g.svg?branch=master)](https://travis-ci.com/edwardoughton/india5g)
[![Coverage Status](https://coveralls.io/repos/github/edwardoughton/India5G/badge.svg)](https://coveralls.io/github/edwardoughton/India5G?branch=master)

This codebase enables 4G and 5G universal broadband strategies to be tested with the ultimate aim of helping to connect more people to a faster internet, as applied here for India.

Please cite the published paper associated with this codebase:

Citation
---------

- Oughton, E.J., and Jha, A.. (2021) Supportive 5G Infrastructure Policies are
Essential for Universal 6G: Assessment Using an Open-Source Techno-Economic Simulation Model Utilizing Remote Sensing. [Forethcoming in IEEE Access](https://arxiv.org/abs/2102.08086).

Importantly, we provide all code (and required data inputs) so that the results can be reproduced. Both unit tests and integration tests are provided for the codebase to ensure reliability.

Method
======
###An Open-Source Techno-Economic 4G & 5G Simulation Model Utilizing Remote Sensing
<p align="center">
  <img src="/figures/method.png" />
</p>


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

You will need numerous input data sets. They are all detailed in the full IEEE paper,
cited above. If there are any additional queries or comments, don't hesitate to reach out
to eoughton [at] gmu [dot] edu for further information.

You will first want to download the Global Administrative Database (GADM), following the link below,  making sure you download the "six separate layers":

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

Preprocess necessary model inputs
=================================

You will need to run various scripts before using the model.

Firstly, run the following to preprocess all the supply and demand data:

    python scripts/preprocess.py

Then you will need to generate the necessary lookup tables, using the provided
cellular system simulation:

    python scripts/sim.py


Using the model
===============

To obtain model results once all inputs have been generated, simply execute the runner script:

    python scripts/run.py

Using the R scripts in the india5G/vis folder, the results are able to be visualized,
reproducing the graphics included in the IEEE paper.


Thanks for the support
======================

**India5G** was written and developed at George Mason University.
