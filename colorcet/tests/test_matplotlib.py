import pytest
import colorcet as cc

pytest.importorskip('matplotlib')

def test_matplotlib_colormaps_available():
    assert len(cc.cm.items()) == 168
    assert len(cc.cm_n.items()) == 52


@pytest.mark.mpl_image_compare
def test_matplotlib():
    import numpy as np
    import matplotlib.pyplot as plt
    xs, _ = np.meshgrid(np.linspace(0, 1, 80), np.linspace(0, 1, 10))
    fig = plt.imshow(xs, cmap=cc.cm.colorwheel).get_figure()
    return fig


@pytest.mark.mpl_image_compare
def test_matplotlib_glasbey():
    import numpy as np
    import matplotlib.pyplot as plt
    xs, _ = np.meshgrid(np.linspace(0, 1, 256), np.linspace(0, 1, 10))
    fig = plt.imshow(xs, cmap=cc.cm.glasbey).get_figure()
    return fig

@pytest.mark.mpl_image_compare
def test_matplotlib_default_colormap_plot_blues():
    hv = pytest.importorskip('holoviews')
    hv.extension('matplotlib')
    fig = hv.render(cc.colormap('blues'), backend='matplotlib')
    return fig