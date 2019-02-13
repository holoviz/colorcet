import pytest  # noqa
import colorcet as cc

def test_bokeh_palettes_available():
    assert len(cc.palette.items()) == 72
    assert len(cc.palette_n.items()) == 21

def test_bokeh_palette_is_a_list():
    assert isinstance(cc.blues, list)
    assert len(cc.blues) == 256
    assert cc.blues[0] == '#f0f0f0'
    assert cc.blues[-1] == '#3a7bb1'
