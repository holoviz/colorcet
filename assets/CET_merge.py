# CET_merge.py - create updated `aliases` and `mapping` for CET_to_py.py
# 1. MATLAB/octave script `make_csvs_from_colorcet.m` must be run first
# 2. Existing `aliases` and `mapping` from CET_to_py.py must be pasted below
# 3. After running script:
#    a. Add the new mapsdir to the `paths` list in CET_to_py.py.
#    b. Replace the existing `aliases` and `mapping` in CET_to_py.py with those printed by this script.
import re
from collections import defaultdict
from CET_updates import new_aliases, new_mapping, new_mapsdir

# paste `aliases` and `mapping` from CET_to_py.py here
aliases = dict()

# paste `mapping` from CET_to_py.py here
mapping = {}

# ## To merge the aliases, we will invert the alias dicts, merge with dict.update, and then invert again back
# ## to a dict of lists.
# invert aliases dict of lists, also new_aliases
old_aliases_inv = {als: k for k, lst in aliases.items() for als in lst}
new_aliases_inv = {als: k for k, lst in new_aliases.items() for als in lst}
# find any conflicts to report later.
aliases_conflicts = []
for alias, descrname in new_aliases_inv.items():
    try:
        if old_aliases_inv[alias] != descrname:
            aliases_conflicts.append((alias, old_aliases_inv[alias], descrname))
    except KeyError:
        pass

# merge the aliases. old aliases taking precedence over new
# This means that Python colorcet aliases may differ slightly from colorcet.m, but will never change meaning.
new_aliases_inv.update(old_aliases_inv)
merged_aliases = defaultdict(list)
[merged_aliases[v].append(k) for k, v in new_aliases_inv.items()]

# ## Update mapping
# First find any conflicts, as these will need to be fixed in aliases
mapping_conflicts = []  # List[Tuple[str, str, str]] # (CET- name, old descriptorname, new descriptorname)
for cet, descr in new_mapping.items():
    if cet in mapping and descr != mapping[cet]:
        mapping_conflicts.append(
            (cet, mapping[cet].replace("-", "_"), new_mapping[cet].replace("-", "_"))
        )
# Merge mapping, with old taking precedence over new
merged_mapping = new_mapping.copy()
merged_mapping.update(mapping)

# for eack mapping conflict, merge aliases under the old name
for _, old, new in mapping_conflicts:
    try:
        merged_aliases[old] += merged_aliases[new]
        del merged_aliases[new]
    except KeyError:
        pass


def print_dict(name, d, braces=False, tabs=0, evenspace=False, sortfn=lambda k: k):
    if evenspace:
        k_maxlen = 0
        for k in d:
            k_maxlen = max(k_maxlen, len(k))
        fmt0 = "{{0:{0:d}s}}".format(k_maxlen)
    else:
        fmt0 = "{0}"
    start = "{" if braces else "dict("
    fmt = ("'{0}': {1}," if braces else "{0} = {1},").format(fmt0, "{1}")
    end = "}" if braces else ")"
    s4 = " " * 4
    tabs = s4 * tabs
    print(tabs + "{0} = {1}".format(name, start))
    for k in sorted(d, key=sortfn):
        val = "'{0}'".format(d[k]) if isinstance(d[k], str) else d[k]
        print(tabs + s4 + fmt.format(k, val))
    print(tabs + end)


def CET_sortfn(k):
    prefix, num, suffix = re.match("(CET-\D+)(\d+)(\D*)", k).groups()
    return "{}{:02d}{}".format(prefix, int(num), suffix)


print("new_mapsdir = '{0}'".format(new_mapsdir))
print_dict("aliases", merged_aliases, evenspace=True)
print_dict("mapping", merged_mapping, braces=True, sortfn=CET_sortfn)
if aliases_conflicts:
    print("#")
    print("# ## NOTICE: Found the following aliases conflicts, with old alias assignment retained over new:")
    print("# ## alias, old_descriptorname, new_descriptorname")
    for als, old, new in aliases_conflicts:
        print("# {}, {}, {}".format(als, old, new))
if mapping_conflicts:
    print("#")
    print("# ## NOTICE: Found the following mapping conflicts, with the CET- name assigned")
    print("# ##         to the original map over the new:")
    print("# ## CET_name, old_descriptorname, new_descriptorname")
    for cet, old, new in mapping_conflicts:
        print("# {}, {}, {}".format(cet, old, new))
if aliases_conflicts or mapping_conflicts:
    print("#")
