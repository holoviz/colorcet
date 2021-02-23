import colorcet as cc
from colorcet.plotting import swatches, sine_combs

import holoviews as hv
import panel as pn

hv.extension('bokeh')

diverging_n = cc.all_original_names(group='diverging', only_aliased=True)
linear_n    = cc.all_original_names(group='linear',    only_aliased=True, not_group='diverging')
cat_n       = cc.all_original_names(group='glasbey',   only_aliased=True)
misc_n      = sorted([k for k in cc.aliases if k not in cat_n + diverging_n + linear_n])

def pane(fn, cmaps):
    return pn.panel(fn(*cmaps, width=400, height=150, cols=1).opts(toolbar=None), linked_axes=False)

diverging_col = pn.Column('#Diverging',   pane(sine_combs, diverging_n))
linear_col    = pn.Column('#Linear',      pane(sine_combs, linear_n))
cat_col       = pn.Column('#Categorical', pane(swatches,   cat_n))
misc_col      = pn.Column('#Misc',        pane(sine_combs, misc_n))

all_named = pn.Row(pn.Column(linear_col,    pn.Spacer(height=102), cat_col),
                   pn.Spacer(width=100),
                   pn.Column(diverging_col, pn.Spacer(height=102), misc_col))

all_named.save('./images/named.png')
