"""
Generate Python versions for each of the colormaps provided in
http://peterkovesi.com/projects/colourmaps/CETperceptual_csv_0_1.zip

Also adds Glasbey colormaps created using: https://github.com/jsignell/glasbey/tree/filtering
see https://github.com/pyviz/colorcet/issues/11 for more details
"""

import os, os.path, csv

paths = ['CETperceptual_csv_0_1', 'Glasbey']
output_file = '../colorcet/__init__.py'
header = '''\
"""
Python versions of the 256-color colormaps provided in
http://peterkovesi.com/projects/colourmaps/CETperceptual_csv_0_1.zip

Each of these colormaps can be accessed as a Bokeh palette or
Matplotlib colormap, either by string name:

  palette['name']
  cm['name']

or as Python attributes:

  palette.name
  cm.name

or as individually importable Python attributes:

  m_name
  b_name

All colormaps are named using Peter Kovesi\'s naming scheme:

<category>_<huesequence>_<lightnessrange>_c<meanchroma>[_s<colorshift>_[r<ifreversed>]]

but some have shorter, more convenient aliases, some of which are
named for the color ranges included and others
based on the qualitative appearance.  The colormaps with
shorter names tend to be the most useful subset, and for
cases like automatic population of a GUI widget these
colormaps are provided as a separate subset:

  palette_n['name'] or palette_n.name
  cm_n['name'] or cm_n.name

Also included are some sets of 256 Glasbey colors. These are available via the
same methods described above and are named:

  glasbey_<starting_palette>[_<min|max>c_<chroma_value>][_<min|max>l_<lightness_value>][_hue_<start>_<end>]

Some of these the glasbey sets are aliased to short names as explained in the User Guide.
"""

__version__ = '1.0.0'

from collections import OrderedDict

class AttrODict(OrderedDict):
    """Ordered dictionary with attribute access (e.g. for tab completion)"""
    def __dir__(self): return self.keys()
    def __delattr__(self, name): del self[name]
    def __getattr__(self, name):
        return self[name] if not name.startswith('_') else super(AttrODict, self).__getattr__(name)
    def __setattr__(self, name, value):
        if (name.startswith('_')): return super(AttrODict, self).__setattr__(name, value)
        self[name] = value

try:
    from matplotlib.colors import LinearSegmentedColormap
    from matplotlib.cm import register_cmap
except:
    def LinearSegmentedColormap(colorlist,name): pass
    def register_cmap(name,cmap): pass
    LinearSegmentedColormap.from_list=lambda n,c,N: None

def rgb_to_hex(r,g,b):
    return '#%02x%02x%02x' % (r,g,b)

def bokeh_palette(name,colorlist):
    palette[name] = [rgb_to_hex(int(r*255),int(g*255),int(b*255)) for r,g,b in colorlist]
    return palette[name]

def mpl_cm(name,colorlist):
    cm[name]      = LinearSegmentedColormap.from_list(name, colorlist, N=len(colorlist))
    register_cmap("cet_"+name, cmap=cm[name])
    return cm[name]

def get_aliases(name):
    """Get the aliases for a given colormap name"""
    for k, v in aliases.items():
        if name == k or name == v:
            name = '{0}, {1}'.format(v, k)
    return name

def all_original_names(group=None, not_group=None, only_aliased=False):
    """Get all original names - optionally in a particular group - or only those with aliases"""
    names = palette.keys()
    if group:
        names = filter(lambda x: group in x, names)
    if not_group:
        names = filter(lambda x: not_group not in x, names)
    if only_aliased:
        names = filter(lambda x: x in aliases.keys(), names)
    else:
        names = filter(lambda x: x not in aliases.values(), names)
    return sorted(list(names))

def colormap(name, cmap=None, bounds=None, array=None,**kwargs):
    """Plot a colormap using matplotlib or bokeh via holoviews"""
    import holoviews as hv; from holoviews import opts

    title = name if cmap else get_aliases(name)
    if bounds is None:
        bounds = (0, 0, 256, 1)
    if array is None:
        import numpy as np
        array = np.meshgrid(np.linspace(0, 1, 256), np.linspace(0, 1, 10))[0]

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

def colormaps(*args, group=None, not_group=None, only_aliased=False, cols=1, **kwargs):
    """Plot colormaps for given names or names in group"""
    import holoviews as hv; from holoviews import opts

    args = args or all_original_names(group=group, not_group=not_group,
                                      only_aliased=only_aliased)
    plot = hv.Layout([
      colormap(arg, **kwargs) if isinstance(arg, str) else
      colormap(*arg, **kwargs) for
      arg in args]).cols(cols)

    backends = hv.Store.loaded_backends()
    if 'matplotlib' in backends:
        plot.opts(opts.Layout(backend='matplotlib', sublabel_format=None,
                              fig_size=kwargs.get('fig_size', 350)))
    return plot

palette = AttrODict()
cm = AttrODict()
palette_n = AttrODict()
cm_n = AttrODict()
'''

footer = """
palette_n = AttrODict(sorted(palette_n.items()))
cm_n = AttrODict(sorted(cm_n.items()))
"""

# Here #mpl indicates a colormap name taken from Matplotlib
aliases = dict(
  cyclic_mygbm_30_95_c78_s25             = 'colorwheel',
  diverging_bkr_55_10_c35                = 'bkr',
  diverging_bky_60_10_c30                = 'bky',
  diverging_bwr_40_95_c42                = 'coolwarm', #mpl
  diverging_gwv_55_95_c39                = 'gwv',
  diverging_linear_bjy_30_90_c45         = 'bjy',
  isoluminant_cgo_80_c38                 = 'isolum',
  linear_bgy_10_95_c74                   = 'bgy',
  linear_bgyw_15_100_c68                 = 'bgyw',
  linear_blue_5_95_c73                   = 'kbc',
  linear_blue_95_50_c20                  = 'blues',    #mpl
  linear_bmw_5_95_c89                    = 'bmw',
  linear_bmy_10_95_c78                   = 'bmy',
  linear_green_5_95_c69                  = 'kgy',
  linear_grey_0_100_c0                   = 'gray',     #mpl
  linear_grey_10_95_c0                   = 'dimgray',
  linear_kryw_0_100_c71                  = 'fire',
  linear_ternary_blue_0_44_c57           = 'kb',
  linear_ternary_green_0_46_c42          = 'kg',
  linear_ternary_red_0_50_c52            = 'kr',
  rainbow_bgyr_35_85_c73                 = 'rainbow',
  glasbey_bw_minc_20                     = 'glasbey',
  glasbey_bw_minc_20_minl_30             = 'glasbey_light',
  glasbey_bw_minc_20_maxl_70             = 'glasbey_dark',
  glasbey_bw_minc_20_hue_330_100         = 'glasbey_warm',
  glasbey_bw_minc_20_hue_150_280         = 'glasbey_cool',
)


with open(output_file, "w") as output:
    output.write(header)
    output.write("aliases = {}\n".format(aliases))
    for path in paths:
      for filename in os.listdir(path):
          if filename.endswith(".csv"):
              base = filename[:-4].replace("-","_").replace("_n256","")
              output.write("\n\n"+base+" = [\\\n")
              with open(os.path.join(path,filename),'r') as csvfile:
                  reader = csv.reader(csvfile)
                  for row in reader:
                      output.write("["+', '.join(row)+"],\n")
              output.write("]\n")
              output.write("b_{0} = bokeh_palette('{0}',{0})\n".format(base))
              output.write("m_{0} = mpl_cm('{0}',{0})\n".format(base))
              output.write("m_{0}_r = mpl_cm('{0}_r',list(reversed({0})))\n".format(base))
              if base in aliases:
                  alias = aliases[base]
                  output.write("{0} = b_{1}\n".format(alias,base))
                  output.write("m_{0} = m_{1}\n".format(alias,base))
                  output.write("m_{0}_r = m_{1}_r\n".format(alias,base))
                  output.write("palette['{0}'] = b_{1}\n".format(alias,base))
                  output.write("palette_n['{0}'] = b_{1}\n".format(alias,base))
                  output.write("cm['{0}'] = m_{1}\n".format(alias,base))
                  output.write("cm['{0}_r'] = m_{1}_r\n".format(alias,base))
                  output.write("cm_n['{0}'] = mpl_cm('{0}',{1})\n".format(alias,base))
                  output.write("cm_n['{0}_r'] = mpl_cm('{0}_r',list(reversed({1})))\n".format(alias,base))
                  output.write("register_cmap('cet_{0}',m_{1})\n".format(alias,base))
                  output.write("register_cmap('cet_{0}_r',m_{1}_r)\n".format(alias,base))
              output.write("\n\n")
    output.write(footer)
