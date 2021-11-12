"""CET_merge.py - Merge new aliases and "cetnames" in CET_updates.py with existing from CET_to_py.py

Instructions
------------

1. Follow instructions at the top of `make_csvs_from_colorcet.m` and then run with MATLAB or GNU Octave to
   generate new colormap CSVs and `CET_updates.py`.
2. Copy `aliases` and `cetnames` from `CET_to_py.py` where noted below.
3. Run `python CET_merge.py` from within its own directory.
4. Copy the resulting terminal output syntax for `aliases` and `cetnames` back into `CET_to_py.py`.
5. Use `git diff` as desired to manually copy-over `#mpl` comments in `aliases`.

Do not commit the copied-in aliases and cetnames dictionaries in this file.

"""

import re
import sys

sys.path.append("../")
from collections import defaultdict

from CET_updates import new_aliases, new_cetnames

# ## Copy aliases and cetnames from CET_to_py.py here:
aliases = {}
cetnames = {}


def find_dict_merge_conflicts(d_to_update, d_updating):
    conflicts = []
    for alias, descrname in d_to_update.items():
        try:
            if d_updating[alias] != descrname:
                conflicts.append((alias, d_updating[alias], descrname))
        except KeyError:
            pass
    return conflicts


def update_aliases(old_aliases, new_aliases):
    # Filter new_aliases to just one alias per name. Old aliases may have more than one alias per name
    new_aliases = {k: v[0:1] for k, v in new_aliases.items()}

    # invert aliases and new_aliases dicts
    old_aliases_inv = {als: k for k, lst in old_aliases.items() for als in lst}
    new_aliases_inv = {als: k for k, lst in new_aliases.items() for als in lst}
    # find any conflicts to report later.
    aliases_conflicts = find_dict_merge_conflicts(new_aliases_inv, old_aliases_inv)

    # merge the aliases. old aliases taking precedence over new
    # This means that Python colorcet aliases may differ slightly from colorcet.m, but will never change meaning.
    merged_aliases_inv = new_aliases_inv.copy()
    merged_aliases_inv.update(old_aliases_inv)
    # "uninvert"
    merged_aliases = defaultdict(list)
    [merged_aliases[v].append(k) for k, v in merged_aliases_inv.items()]

    return merged_aliases, aliases_conflicts


def update_cetnames(old_cetnames, new_cetnames):
    # cetnames merge is a simple dict update. Still should check for conflicts
    cetnames_conflicts = find_dict_merge_conflicts(new_cetnames, old_cetnames)
    merged_cetnames = new_cetnames.copy()
    merged_cetnames.update(old_cetnames)
    return merged_cetnames, cetnames_conflicts


def print_dict(name, d, braces=False, tabs=0, evenspace=False, sortfn=None):
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
    keys = d.keys()
    if sortfn:
        keys = sorted(keys, key=sortfn)
    for k in keys:
        val = "'{0}'".format(d[k]) if isinstance(d[k], str) else d[k]
        print(tabs + s4 + fmt.format(k, val))
    print(tabs + end)


cetname_sort_re = re.compile(r"CET-(\D+)(\d+)(\D?)")


def cetname_sortfn(cetname):
    prefix, num, suffix = cetname_sort_re.match(cetname).groups()
    return prefix, int(num), suffix


if __name__ == "__main__":
    # Update aliases
    aliases, aliases_conflicts = update_aliases(aliases, new_aliases)
    cetnames, cetnames_conflicts = update_cetnames(cetnames, new_cetnames)

    print_dict("aliases", aliases, evenspace=True, sortfn=lambda k: k)
    print_dict("cetnames", cetnames, braces=True, sortfn=cetname_sortfn)
    if aliases_conflicts:
        print("#")
        print("# ## NOTICE: Found the following aliases conflicts, with old alias assignment retained over new:")
        print("# ## alias, old_descriptorname, new_descriptorname")
        for als, old, new in aliases_conflicts:
            print("# {}, {}, {}".format(als, old, new))
    if cetnames_conflicts:
        print("#")
        print("# ## NOTICE: Found the following cetnames conflicts, with old cetname assignment retained over new:")
        print("# ## cetname, old_descriptorname, new_descriptorname")
        for name, old, new in cetnames_conflicts:
            print("# {}, {}, {}".format(name, old, new))
