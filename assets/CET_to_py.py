"""
Generate Python versions for each of the colormaps provided in
http://peterkovesi.com/projects/colourmaps/CETperceptual_csv_0_1.zip

Also adds Glasbey colormaps created using: https://github.com/taketwo/glasbey
see https://github.com/pyviz/colorcet/issues/11 for more details
"""

import os, os.path, csv

paths = ['CETperceptual_csv_0_1', 'CETperceptual_csv_0_1_v2', 'Glasbey']
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

Some of the Glasbey sets are aliased to short names as explained in the User Guide.
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
    cm[name] = LinearSegmentedColormap.from_list(name, colorlist, N=len(colorlist))
    register_cmap("cet_"+name, cmap=cm[name])
    return cm[name]

def get_aliases(name):
    """Get the aliases for a given colormap name"""
    names = [name]

    def check_aliases(names, d,  k_position=-1, v_position=0):
        for name in [n for n in names]:
            for k, v in d.items():
                if name == v and k not in names:
                    if k_position == -2:
                        names.append(k)
                    else:
                        names.insert(k_position, k)
                if name == k and v not in names:
                    if v_position == -2:
                        names.append(v)
                    else:
                        names.insert(v_position, v)
        return names

    names = check_aliases(names, aliases, k_position=-2, v_position=0)
    names = check_aliases(names, aliases_v2, k_position=-1, v_position=-2)
    names = check_aliases(names, mapping_flipped, k_position=-2, v_position=-1)
    names = check_aliases(names, aliases_v2, k_position=-1, v_position=-2)
    names = check_aliases(names, aliases, k_position=-2, v_position=0)
    return ',  '.join(names)

def all_original_names(group=None, not_group=None, only_aliased=False, only_CET=False):
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
    if only_CET:
        names = filter(lambda x: x in mapping_flipped.values(), names)
    else:
        names = filter(lambda x: x not in mapping_flipped.values(), names)
    return sorted(list(names))

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
    cyclic_mygbm_30_95_c78_s25                      = 'colorwheel',
    diverging_bkr_55_10_c35                         = 'bkr',
    diverging_bky_60_10_c30                         = 'bky',
    diverging_protanopic_deuteranopic_bwy_60_95_c32 = 'bwy',
    diverging_tritanopic_cwr_75_98_c20              = 'cwr',
    diverging_bwr_40_95_c42                         = 'coolwarm', #mpl
    diverging_gwv_55_95_c39                         = 'gwv',
    diverging_linear_bjy_30_90_c45                  = 'bjy',
    isoluminant_cgo_80_c38                          = 'isolum',
    linear_bgy_10_95_c74                            = 'bgy',
    linear_bgyw_15_100_c68                          = 'bgyw',
    linear_blue_5_95_c73                            = 'kbc',
    linear_blue_95_50_c20                           = 'blues',    #mpl
    linear_bmw_5_95_c89                             = 'bmw',
    linear_bmy_10_95_c78                            = 'bmy',
    linear_green_5_95_c69                           = 'kgy',
    linear_grey_0_100_c0                            = 'gray',     #mpl
    linear_grey_10_95_c0                            = 'dimgray',
    linear_kryw_0_100_c71                           = 'fire',
    linear_ternary_blue_0_44_c57                    = 'kb',
    linear_ternary_green_0_46_c42                   = 'kg',
    linear_ternary_red_0_50_c52                     = 'kr',
    rainbow_bgyr_35_85_c73                          = 'rainbow',
    glasbey_bw_minc_20                              = 'glasbey',
    glasbey_bw_minc_20_minl_30                      = 'glasbey_light',
    glasbey_bw_minc_20_maxl_70                      = 'glasbey_dark',
    glasbey_bw_minc_20_hue_330_100                  = 'glasbey_warm',
    glasbey_bw_minc_20_hue_150_280                  = 'glasbey_cool',
)

# Mapping maps the short "CET" names to longer descriptor names
mapping = {
    'CET-L1': 'linear_grey_0-100_c0',
    'CET-L2': 'linear_grey_10-95_c0',
    'CET-L3': 'linear_kryw_0-100_c71',
    'CET-L4': 'linear_kry_0-97_c73',
    'CET-L5': 'linear_kgy_5-95_c69',
    'CET-L6': 'linear_kbc_5-95_c73',
    'CET-L7': 'linear_bmw_5-95_c86',
    'CET-L8': 'linear_bmy_10-95_c71',
    'CET-L9': 'linear_bgyw_20-98_c66',
    'CET-L10': 'linear_gow_60-85_c27',
    'CET-L11': 'linear_gow_65-90_c35',
    'CET-L12': 'linear_blue_95-50_c20',
    'CET-L13': 'linear_ternary-red_0-50_c52',
    'CET-L14': 'linear_ternary-green_0-46_c42',
    'CET-L15': 'linear_ternary-blue_0-44_c57',
    'CET-L16': 'linear_kbgyw_5-98_c62',
    'CET-L17': 'linear_worb_100-25_c53',
    'CET-L18': 'linear_wyor_100-45_c55',
    'CET-L19': 'linear_wcmr_100-45_c42',
    'CET-D1': 'diverging_bwr_40-95_c42',
    'CET-D1A': 'diverging_bwr_20-95_c54',
    'CET-D2': 'diverging_gwv_55-95_c39',
    'CET-D3': 'diverging_gwr_55-95_c38',
    'CET-D4': 'diverging_bkr_55-10_c35',
    'CET-D6': 'diverging_bky_60-10_c30',
    'CET-D7': 'diverging-linear_bjy_30-90_c45',
    'CET-D8': 'diverging-linear_bjr_30-55_c53',
    'CET-D9': 'diverging_bwr_55-98_c37',
    'CET-D10': 'diverging_cwm_80-100_c22',
    'CET-D13': 'diverging_bwg_20-95_c41',
    'CET-R3': 'diverging-rainbow_bgymr_45-85_c67',
    'CET-R1': 'rainbow_bgyrm_35-85_c69',
    'CET-R2': 'rainbow_bgyr_35-85_c72',
    'CET-C1': 'cyclic_mrybm_35-75_c68',
    'CET-C1s': 'cyclic_mrybm_35-75_c68_s25',
    'CET-C2': 'cyclic_mygbm_30-95_c78',
    'CET-C2s': 'cyclic_mygbm_30-95_c78_s25',
    'CET-C4': 'cyclic_wrwbw_40-90_c42',
    'CET-C4s': 'cyclic_wrwbw_40-90_c42_s25',
    'CET-C5': 'cyclic_grey_15-85_c0',
    'CET-C5s': 'cyclic_grey_15-85_c0_s25',
    'CET-I1': 'isoluminant_cgo_70_c39',
    'CET-I2': 'isoluminant_cgo_80_c38',
    'CET-I3': 'isoluminant_cm_70_c39',
    'CET-D11': 'diverging-isoluminant_cjo_70_c25',
    'CET-D12': 'diverging-isoluminant_cjm_75_c23',
    'CET-CBL1': 'linear-protanopic-deuteranopic_kbjyw_5-95_c25',
    'CET-CBL2': 'linear-protanopic-deuteranopic_kbw_5-98_c40',
    'CET-CBD1': 'diverging-protanopic-deuteranopic_bwy_60-95_c32',
    'CET-CBC1': 'cyclic-protanopic-deuteranopic_bwyk_16-96_c31',
    'CET-CBC2': 'cyclic-protanopic-deuteranopic_wywb_55-96_c33',
    'CET-CBTL1': 'linear-tritanopic_krjcw_5-98_c46',
    'CET-CBTL2': 'linear-tritanopic_krjcw_5-95_c24',
    'CET-CBTD1': 'diverging-tritanopic_cwr_75-98_c20',
    'CET-CBTC1': 'cyclic-tritanopic_cwrk_40-100_c20',
    'CET-CBTC2': 'cyclic-tritanopic_wrwc_70-100_c20',
}

# mapping_flipped is the inverse dict of mapping, with underscores replacing all hyphens
mapping_flipped = {v.replace('-', '_'): k.replace('-', '_') for
                   k, v in mapping.items()}

aliases_v2 = {
    'linear_green_5_95_c69': 'linear_kgy_5_95_c69',
    'linear_blue_5_95_c73': 'linear_kbc_5_95_c73',
}

def create_alias(alias, base, output, is_name=True):
    output.write("{0} = b_{1}\n".format(alias,base))
    output.write("m_{0} = m_{1}\n".format(alias,base))
    output.write("m_{0}_r = m_{1}_r\n".format(alias,base))
    output.write("palette['{0}'] = b_{1}\n".format(alias,base))
    if is_name:
        output.write("palette_n['{0}'] = b_{1}\n".format(alias,base))
    output.write("cm['{0}'] = m_{1}\n".format(alias,base))
    output.write("cm['{0}_r'] = m_{1}_r\n".format(alias,base))
    if is_name:
        output.write("cm_n['{0}'] = mpl_cm('{0}',{1})\n".format(alias,base))
        output.write("cm_n['{0}_r'] = mpl_cm('{0}_r',list(reversed({1})))\n".format(alias,base))
    else:
        output.write("register_cmap('cet_{0}',m_{1})\n".format(alias,base))
        output.write("register_cmap('cet_{0}_r',m_{1}_r)\n".format(alias,base))

cmaps = []
with open(output_file, "w") as output:
    output.write(header)
    output.write("aliases = {}\n".format(aliases))
    output.write("aliases_v2 = {}\n".format(aliases_v2))
    output.write("mapping_flipped = {}\n".format(mapping_flipped))
    for path in paths:
        for filename in os.listdir(path):
            if filename.endswith(".csv"):
                base = mapping.get(filename[:-4], filename[:-4])
                base = base.replace("-","_").replace("_n256","")
                # `base` is the descriptorname from colorcet.m with hyphens as underscores and without _n256
                if base in cmaps:
                    continue
                output.write("\n\n"+base+" = [\\\n")
                # Convert the CSV to an 256x3 list of lists.
                with open(os.path.join(path,filename),'r') as csvfile:
                    reader = csv.reader(csvfile)
                    for row in reader:
                        output.write("["+', '.join(row)+"],\n")
                output.write("]\n")
                # Create the bokeh pallete and matplotlib colormap & reverse colormap
                output.write("b_{0} = bokeh_palette('{0}',{0})\n".format(base))
                output.write("m_{0} = mpl_cm('{0}',{0})\n".format(base))
                output.write("m_{0}_r = mpl_cm('{0}_r',list(reversed({0})))\n".format(base))
                # Create aliases
                if base in aliases:
                    alias = aliases[base]
                    create_alias(alias, base, output)
                if base in mapping_flipped:
                    alias = mapping_flipped[base]
                    create_alias(alias, base, output, is_name=False)
                output.write("\n\n")
                cmaps.append(base)
    output.write(footer)
