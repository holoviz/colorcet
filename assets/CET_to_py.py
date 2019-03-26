"""
Generate Python versions for each of the colormaps provided in
http://peterkovesi.com/projects/colourmaps/CETperceptual_csv_0_1.zip

Also adds Glasbey colormaps created using: https://github.com/taketwo/glasbey.git
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
inspired by Matplotlib colormaps with similar names and others
based on the qualitative appearance.  The colormaps with
shorter names tend to be the most useful subset, and for
cases like automatic population of a GUI widget these
colormaps are provided as a separate subset:

  palette_n['name'] or palette_n.name
  cm_n['name'] or cm_n.name

Also included are some sets of 256 Glasbey colors. These are available via the
same methods described above and are named:

  glasbey_<starting_palette>[_no_black<if_no_black>]

The no_black versions are aliased to their starting palette names.
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
  glasbey_bw_no_black                    = 'glasbey',
  glasbey_category10_no_black            = 'Category10',  #bokeh
  glasbey_category20_no_black            = 'Category20',  #bokeh
)


with open(output_file, "w") as output:
    output.write(header)
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
