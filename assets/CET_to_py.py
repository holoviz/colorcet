"""
Generate Python versions for each of the colormaps provided in
http://peterkovesi.com/projects/colourmaps/CETperceptual_csv_0_1.zip
"""
# The linear_kryw_mycarta map is from
# https://mycarta.wordpress.com/2012/10/14/the-rainbow-is-deadlong-live-the-rainbow-part-4-cie-lab-heated-body/

import os, os.path, csv

path = 'CETperceptual_csv_0_1'
output_file = '../cetcolors/__init__.py'
header = '''\
"""
Python versions of the 256-color colormaps provided in
http://peterkovesi.com/projects/colourmaps/CETperceptual_csv_0_1.zip

Each of these colormaps can be accessed as a Bokeh palette or
Matplotlib colormap, either by string name:

  palette['name']
  cm['name']

or as Python attributes:

  m_name
  b_name

All colormaps are named using Peter Kovesi\'s naming scheme:

<category>_<huesequence>_<lightnessrange>_c<meanchroma>[_s<colorshift>_[r<ifreversed>]]

but some have shorter, more convenient aliases, some of which are 
inspired by Matplotlib colormaps of the same name and others
based on the qualitative appearance.
"""

__version__ = '0.9.0'

from collections import OrderedDict
try:
    from matplotlib.colors import LinearSegmentedColormap
    from matplotlib.cm import register_cmap
except:
    def LinearSegmentedColormap(colorlist,name): pass
    def register_cmap(name,cmap): pass

def rgb_to_hex(r,g,b):
    return '#%02x%02x%02x' % (r,g,b) 

def bokeh_palette(name,colorlist):
    palette[name] = [rgb_to_hex(int(r*255),int(g*255),int(b*255)) for r,g,b in colorlist]
    return palette[name]

def mpl_cm(name,colorlist):
    cm[name]      = LinearSegmentedColormap.from_list(name, colorlist, N=len(colorlist))
    register_cmap("cet_"+name, cmap=cm[name])
    return cm[name]

palette = OrderedDict()
cm = OrderedDict()
'''

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
  linear_bmy_10_95_c78                   = 'inferno',  #mpl
  linear_green_5_95_c69                  = 'kgy',
  linear_grey_0_100_c0                   = 'gray',     #mpl
  linear_grey_10_95_c0                   = 'dimgray',
  linear_kryw_0_100_c71                  = 'fire',      #mpl
  linear_ternary_blue_0_44_c57           = 'kb',
  linear_ternary_green_0_46_c42          = 'kg',
  linear_ternary_red_0_50_c52            = 'kr',
  rainbow_bgyr_35_85_c73                 = 'rainbow',
)


with open(output_file, "w") as output:
    output.write(header)
    for filename in os.listdir(path):
        if filename.endswith(".csv"):
            base = filename[:-4].replace("-","_").replace("_n256","")
            output.write("\n\n"+base+" = [\\\n")
            with open(os.path.join(path,filename),'rb') as csvfile:
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
                output.write("cm['{0}'] = m_{1}\n".format(alias,base))
                output.write("cm['{0}_r'] = m_{1}_r\n".format(alias,base))
                output.write("register_cmap('cet_{0}',m_{1})\n".format(alias,base))
                output.write("register_cmap('cet_{0}_r',m_{1}_r)\n".format(alias,base))
            output.write("\n\n")
