<img src="https://github.com/holoviz/colorcet/blob/master/doc/_static/logo.png" width=200><br>

-----------------

# Colorcet: Collection of perceptually uniform colormaps

|    |    |
| --- | --- |
| Build Status | [![Linux/MacOS Build Status](https://github.com/holoviz/colorcet/workflows/tests/badge.svg?query=branch%3Amaster)](https://github.com/holoviz/colorcet/actions/workflows/tests.yaml?query=branch%3Amaster) |
| Coverage | [![codecov](https://codecov.io/gh/holoviz/colorcet/branch/master/graph/badge.svg)](https://codecov.io/gh/holoviz/colorcet) ||
| Latest dev release | [![Github tag](https://img.shields.io/github/tag/holoviz/colorcet.svg?label=tag&colorB=11ccbb)](https://github.com/holoviz/colorcet/tags) [![dev-site](https://img.shields.io/website-up-down-green-red/https/pyviz-dev.github.io/colorcet.svg?label=dev%20website)](https://pyviz-dev.github.io/colorcet/) |
| Latest release | [![Github release](https://img.shields.io/github/release/holoviz/colorcet.svg?label=tag&colorB=11ccbb)](https://github.com/holoviz/colorcet/releases) [![PyPI version](https://img.shields.io/pypi/v/colorcet.svg?colorB=cc77dd)](https://pypi.python.org/pypi/colorcet) [![colorcet version](https://img.shields.io/conda/v/holoviz/colorcet.svg?colorB=4488ff&style=flat)](https://anaconda.org/holoviz/colorcet) [![conda-forge version](https://img.shields.io/conda/v/conda-forge/colorcet.svg?label=conda%7Cconda-forge&colorB=4488ff)](https://anaconda.org/conda-forge/colorcet) [![defaults version](https://img.shields.io/conda/v/anaconda/colorcet.svg?label=conda%7Cdefaults&style=flat&colorB=4488ff)](https://anaconda.org/anaconda/colorcet) |
| Python | [![Python support](https://img.shields.io/pypi/pyversions/colorcet.svg)](https://pypi.org/project/colorcet/) |
| Docs | [![gh-pages](https://img.shields.io/github/last-commit/holoviz/colorcet/gh-pages.svg)](https://github.com/holoviz/colorcet/tree/gh-pages) [![site](https://img.shields.io/website-up-down-green-red/http/colorcet.holoviz.org.svg)](http://colorcet.holoviz.org) |


## What is it?

Colorcet is a collection of
perceptually uniform colormaps for use with Python plotting programs like
[bokeh](http://bokeh.pydata.org),
[matplotlib](http://matplotlib.org),
[holoviews](http://holoviews.org), and
[datashader](https://github.com/bokeh/datashader) based on the
set of [perceptually uniform colormaps](https://arxiv.org/abs/1509.03700) created
by Peter Kovesi at the Center for Exploration Targeting.


## Installation

Colorcet supports Python 2.7, 3.6, 3.7, 3.8, 3.9 and 3.10  on Linux, Windows, or Mac
and can be installed with conda:

```sh
conda install colorcet
```

or with pip:

```sh
python -m pip install colorcet
```

Once installed you can copy the examples into the current directory using the colorcet command and run them using the Jupyter notebook:

```sh
colorcet examples
cd colorcet-examples
jupyter notebook
```

(Here colorcet examples is a shorthand for colorcet copy-examples --path colorcet-examples && colorcet fetch-data --path colorcet-examples.)

To work with JupyterLab you will also need the PyViz JupyterLab extension:

```sh
conda install -c conda-forge jupyterlab
jupyter labextension install @pyviz/jupyterlab_pyviz
```

Once you have installed JupyterLab and the extension launch it with:

```sh
jupyter-lab
```

If you want to try out the latest features between releases, you can get the latest dev release by installing:

```sh
conda install -c pyviz/label/dev colorcet
```

For more information take a look at [Getting Started](http://colorcet.holoviz.org/getting_started).

## Learning more

You can see all the details about the methods used to create these
colormaps in [Peter Kovesi's 2015 arXiv
paper](https://arxiv.org/pdf/1509.03700v1.pdf).  Other useful
background is available in a [1996 paper from
IBM](http://www.research.ibm.com/people/l/lloydt/color/color.HTM).

The Matplotlib project also has a number of relevant resources,
including an excellent
[2015 SciPy talk](https://www.youtube.com/watch?v=xAoljeRJ3lU), the
[viscm tool for creating maps like the four in mpl](https://github.com/matplotlib/viscm), the
[cmocean site](http://matplotlib.org/cmocean/) collecting a set of maps created by viscm,
and the [discussion of how the mpl maps were created](https://bids.github.io/colormap/).


## Samples

Some of the Colorcet colormaps that have short, memorable names (which are probably
the most useful ones) are visible here:

<img src="./examples/assets/images/named.png" width="800">

But the complete set of 100+ is shown in the [User Guide](http://colorcet.holoviz.org/user_guide).
