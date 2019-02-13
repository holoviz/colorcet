import pytest
import colorcet as cc

def test_matplotlib_colormaps_available():
    pytest.importorskip('matplotlib')
    assert len(cc.cm.items()) == 144
    assert len(cc.cm_n.items()) == 42


@pytest.mark.mpl_image_compare
def test_matplotlib():
    pytest.importorskip('matplotlib')
    import numpy as np
    import matplotlib.pyplot as plt
    xs, _ = np.meshgrid(np.linspace(0, 1, 80), np.linspace(0, 1, 10))
    fig = plt.imshow(xs, cmap=cc.cm.colorwheel).get_figure()
    return fig
