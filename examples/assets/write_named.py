import colorcet as cc
import numpy as np

import holoviews as hv
from holoviews import opts

import panel as pn

hv.extension('bokeh')

xs, _ = np.meshgrid(np.linspace(0, 1, 256), np.linspace(0, 1, 10))

def colormap(name, cmap=None, bounds=(0, 0, 256, 1), array=xs, **kwargs):
    if cmap is None:
        cmap = cc.palette[name]
    options = opts.Image(xaxis=None, yaxis=None, width=400, height=150, cmap=cmap, toolbar=None, **kwargs)
    return hv.Image(array, bounds=bounds, group=name).opts(options)
   
sine = np.load("./colourmaptest.npy")

def get_names_for_group(group='diverging'):
    palettes = [v for k, v in cc.palette.items() if group in k]
    return sorted([k for k, v in cc.palette_n.items() if v in palettes])
    
diverging_n = get_names_for_group('diverging')
diverging_col = pn.Column('#Diverging', *[colormap(c, array=sine) for c in diverging_n])

linear_n = get_names_for_group('linear')
linear_col = pn.Column('#Linear', *[colormap(c, array=sine) for c in linear_n])

cat_n = get_names_for_group('glasbey')
cat_col = pn.Column('#Categorical', *[colormap(c) for c in cat_n])

misc_n = sorted([k for k in cc.palette_n.keys() if k not in cat_n + diverging_n + linear_n])
misc_col = pn.Column('#Misc', *[colormap(c, array=sine) for c in misc_n])

all_named = pn.Row(
    linear_col, pn.Spacer(width=100), 
    pn.Column(
        diverging_col, pn.Spacer(height=102), 
        cat_col, pn.Spacer(height=102), 
        misc_col))

all_named.save('./images/named.png')