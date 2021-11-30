***************
Getting started
***************

Installation
------------

Colorcet supports Python 2.7, 3.6, 3.7, 3.8 and 3.9 on Linux, Windows, or Mac
and can be installed with conda::

    conda install colorcet

or with pip::

    pip install colorcet

Usage
-----

Once you've installed colorcet the colormaps will be available
in two formats:

1.  A Bokeh-style palette, i.e., a Python list of RGB colors as hex
    strings, like \['\#000000', ..., '\#ffffff'\]
2.  A Matplotlib LinearSegmentedColormap using normalized magnitudes,
    like LinearSegmentedColormap.from\_list("fire",\[ \[0.0,0.0,0.0\],
    ..., \[1.0,1.0,1.0\] \], 256)

Import colorcet and use the new colormaps anywhere you would use a
regular colormap.

**Matplotlib**::

    import numpy as np
    import colorcet as cc
    import matplotlib.pyplot as plt

    xs, _ = np.meshgrid(np.linspace(0, 1, 80), np.linspace(0, 1, 10))
    plt.imshow(xs, cmap=cc.cm.colorwheel);  # use tab completion to choose

**Bokeh**::

    import numpy as np
    import colorcet as cc
    from bokeh.plotting import figure, show

    xs, _ = np.meshgrid(np.linspace(0, 1, 80), np.linspace(0, 1, 10))
    p = figure(x_range=(0, 80), y_range=(0, 10), height=100, width=400)

    p.image(image=[xs], x=0, y=0, dw=80, dh=10, palette=cc.fire)  # use tab completion to choose
    show(p)

If you have any questions, please refer to the `User Guide <../user_guide/index>`_
and if that doesn't help, feel free to post an issue on GitHub, question on stackoverflow,
or discuss on Gitter.

Developer Instructions
----------------------

1. Install Python 3 `miniconda <https://docs.conda.io/en/latest/miniconda.html>`_ or `anaconda <https://www.anaconda.com/products/individual/>`_, if you don't already have it on your system.

2. Clone the colorcet git repository if you do not already have it::

    git clone git://github.com/pyviz/colorcet.git

3. Set up a new conda environment with optional plotting tools::

    cd colorcet
    conda env create -n colorcet matplotlib bokeh holoviews
    conda activate colorcet

4. Put the colorcet directory into the Python path in this environment::

    pip install -e .
