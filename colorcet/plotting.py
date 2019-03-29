import numpy as np
import holoviews as hv
from holoviews import opts

from . import get_aliases, all_original_names, palette, cm

array = np.meshgrid(np.linspace(0, 1, 256), np.linspace(0, 1, 10))[0]

def swatch(name, cmap=None, bounds=None, array=array, **kwargs):
    """Show swatch using matplotlib or bokeh via holoviews"""
    title = name if cmap else get_aliases(name)
    if bounds is None:
        bounds = (0, 0, 256, 1)

    plot = hv.Image(array, bounds=bounds, group=title)
    backends = hv.Store.loaded_backends()
    if 'bokeh' in backends:
        plot.opts(opts.Image(backend='bokeh', width=900, height=100, toolbar='above',
                             default_tools=['xwheel_zoom', 'xpan', 'save', 'reset'],
                             cmap=cmap or palette[name]))
    if 'matplotlib' in backends:
        plot.opts(opts.Image(backend='matplotlib', aspect=15, fig_size=350,
                             cmap=cmap or cm[name]))
    return plot.opts(opts.Image(xaxis=None, yaxis=None), opts.Image(**kwargs))

def swatches(*args, group=None, not_group=None, only_aliased=False, cols=1, **kwargs):
    """Show swatches for given names or names in group"""
    args = args or all_original_names(group=group, not_group=not_group,
                                      only_aliased=only_aliased)
    plot = hv.Layout([
      swatch(arg, **kwargs) if isinstance(arg, str) else
      swatch(*arg, **kwargs) for
      arg in args]).cols(cols)

    backends = hv.Store.loaded_backends()
    if 'matplotlib' in backends:
        plot.opts(opts.Layout(backend='matplotlib', sublabel_format=None,
                              fig_size=kwargs.get('fig_size', 350)))
    return plot

arr = np.arange(0, 100)
np.random.shuffle(arr)
zz = arr.reshape(10, 10)
xx, yy = np.meshgrid(np.arange(0,10), np.arange(0,10))

data = np.array([xx, yy, zz]).transpose().reshape(100, 3)

def candy_buttons(name, cmap=None, size=450, **kwargs):
    if cmap is None:
        cmap = palette[name][:100]
        name = get_aliases(name)
    options = opts.Points(color='color', size=size/13.0, tools=['hover'],
                          yaxis=None, xaxis=None, height=size, width=size,
                          cmap=cmap, **kwargs)
    return hv.Points(data, vdims='color').opts(options).relabel(name)