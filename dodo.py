"""
This file provides a mechanism to map between the semantic commands that any
project has (build docs, run tests, copy examples ... ) and the specific
command that should be run.

Most of these commands are stored in pyctdev which is essentially a collection
of the pyviz way of doing these actions. Commands that are newer, or specific
to a particular project, will live in this file instead. To see a list of
all the available commands - after installing pyctdev - run:

$ doit list

To run one command, for instance building the website, run:

$ doit build_website
"""

import os
if "PYCTDEV_ECOSYSTEM" not in os.environ:
    os.environ["PYCTDEV_ECOSYSTEM"] = "conda"
from pyctdev import * # noqa: api


def task_build_website():
    return {'actions': [
        "nbsite generate-rst --org pyviz --project-name colorcet --offset 0",
        "nbsite build --what=html --output=builtdocs",
    ]}
