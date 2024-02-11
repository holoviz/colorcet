"""rename_CET_maps.py

Convert CET-*.csv files to descriptornames using `mapping` from CET_to_py.py and `git mv` them to a single
folder.

This was run in the assets/ dir on holoviz/colorcet commit 1dad8be
"""

from pathlib import Path
import subprocess

from CET_to_py import mapping

CET_csvs = Path("CETperceptual_csv_0_1_v2").glob("*.csv")
orig_path = Path("CETperceptual_csv_0_1")

newnames = []
for path in CET_csvs:
    try:
        name = mapping[path.stem]
    except KeyError:
        print(f"No match for {path.stem}")
        continue
    if "_s25" in name:
        name = name.replace("_s25", "_n256_s25")
    else:
        name += "_n256"
    new_name = f"{name}.csv"
    newnames.append(new_name)
    new_path = orig_path / new_name
    subprocess.run(f'git mv -vk "{path}" "{new_path}"', shell=True)

subprocess.run("git rm -rf CETperceptual_csv_0_1_v2", shell=True)
