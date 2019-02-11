import os
if "PYCTDEV_ECOSYSTEM" not in os.environ:
    os.environ["PYCTDEV_ECOSYSTEM"] = "conda"
from pyctdev import * # noqa: api


def task_build_website():
    return {'actions': [
        "nbsite generate-rst --org pyviz --project-name colorcet --offset 0",
        "nbsite build --what=html --output=builtdocs",
    ]}
