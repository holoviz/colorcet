import os
import sys
import shutil
from setuptools import setup, find_packages

import pyct.build

def get_setup_version(reponame):
    """
    Helper to get the current version from either git describe or the
    .version file (if available).
    """
    import json
    basepath = os.path.split(__file__)[0]
    version_file_path = os.path.join(basepath, reponame, '.version')
    try:
        from colorcet import version
    except:
        version = None
    if version is not None:
        return version.Version.setup_version(basepath, reponame, archive_commit="$Format:%h$")
    else:
        return json.load(open(version_file_path, 'r'))['version_string']


########## dependencies ##########

install_requires = [
    'pyct >=0.4.4',
]

examples = [
    'numpy',
    'holoviews',
    'matplotlib',
    'bokeh',
]

tests = [
    'flake8',
    'nbsmoke >=0.2.6',
    'pytest >=2.8.5',
    'pytest-cov',
    'packaging',
]

extras_require = {
    'tests': tests,
    'examples': examples,
    'doc': examples + [
        'nbsite >=0.8.4',
        'sphinx-copybutton',
    ],
    'tests_extra': tests + [
        'pytest-mpl'  # only available on pip and conda-forge
    ],
    # until pyproject.toml/equivalent is widely supported (setup_requires
    # doesn't work well with pip)
    'build': [
        'pyct >=0.4.4',
        'setuptools >=30.3.0',
        'wheel',
    ]
}

extras_require['all'] = sorted(set(sum(extras_require.values(), [])))

setup_args = dict(
    name='colorcet',
    description='Collection of perceptually uniform colormaps',
    version=get_setup_version('colorcet'),
    long_description=open("README.md", mode="r", encoding="utf-8").read(),
    long_description_type='text/markdown',
    license_files=['LICENSE.txt'],
    license='CC-BY License',
    classifiers=[
        "License :: OSI Approved",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Development Status :: 5 - Production/Stable",
    ],
    author="James A. Bednar",
    author_email="jbednar@anaconda.com",
    maintainer="James A. Bednar",
    maintainer_email="jbednar@anaconda.com",
    url="https://colorcet.holoviz.org",
    project_urls = {
        "Bug Tracker": "http://github.com/holoviz/colorcet/issues",
        "Documentation": "https://colorcet.holoviz.org",
        "Source Code": "http://github.com/holoviz/colorcet",
    },
    include_package_data=True,
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=install_requires,
    extras_require=extras_require,
    entry_points={
        'console_scripts': [
            'colorcet = colorcet.__main__:main'
        ]
    },
)


if __name__=="__main__":
    example_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                'colorcet','examples')
    if 'develop' not in sys.argv:
        pyct.build.examples(example_path, __file__, force=True)

    setup(**setup_args)

    if os.path.isdir(example_path):
        shutil.rmtree(example_path)
