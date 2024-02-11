import colorcet as cc
from colorcet.plotting import swatches, sine_combs

import holoviews as hv
import panel as pn

hv.extension('bokeh')

diverging_n = cc.all_original_names(group='diverging', only_aliased=True)
linear_n = cc.all_original_names(group='linear', not_group='diverging', only_aliased=True)
cat_n = cc.all_original_names(group='glasbey', only_aliased=True)
misc_n = sorted([k for k in cc.aliases if k not in cat_n + diverging_n + linear_n])

diverging_col = pn.Column('#Diverging', sine_combs(*diverging_n, width=400, height=150).opts(toolbar=None))
linear_col = pn.Column('#Linear', sine_combs(*linear_n, width=400, height=150).opts(toolbar=None))
cat_col = pn.Column('#Categorical', swatches(*cat_n, width=400, height=150, cols=1).opts(toolbar=None))
misc_col = pn.Column('#Misc', sine_combs(*misc_n, width=400, height=150).opts(toolbar=None))

all_named = pn.Row(
    linear_col, pn.Spacer(width=100),
    pn.Column(
        diverging_col, pn.Spacer(height=102),
        cat_col, pn.Spacer(height=102),
        misc_col))

all_named.save('./images/named.png')
