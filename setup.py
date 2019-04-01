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
        from param import version
    except:
        version = None
    if version is not None:
        return version.Version.setup_version(basepath, reponame, archive_commit="$Format:%h$")
    else:
        print("WARNING: param>=1.6.0 unavailable. If you are installing a package, this warning can safely be ignored. If you are creating a package or otherwise operating in a git repository, you should install param>=1.6.0.")
        return json.load(open(version_file_path, 'r'))['version_string']


########## dependencies ##########

install_requires = [
    'param >=1.7.0',
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
]

extras_require = {
    'tests': tests,
    'examples': examples,
    'doc': examples + [
        'nbsite',
        'sphinx_ioam_theme',
    ],
    'tests_extra': tests + [
        'pytest-mpl'  # only available on pip and conda-forge
    ],
    # until pyproject.toml/equivalent is widely supported (setup_requires
    # doesn't work well with pip)
    'build': [
        'param >=1.7.0',
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
    long_description='README.md',
    long_description_type='text/markdown',
    license_file='LICENSE.txt',
    license='CC-BY License',
    classifiers=[
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Development Status :: 5 - Production/Stable",
    ],
    author="James A. Bednar",
    author_email="jbednar@anaconda.com",
    maintainer="James A. Bednar",
    maintainer_email="jbednar@anaconda.com",
    url="https://colorcet.pyviz.org",
    project_urls = {
        "Bug Tracker": "http://github.com/pyviz/colorcet/issues",
        "Documentation": "https://colorcet.pyviz.org",
        "Source Code": "http://github.com/pyviz/colorcet",
    },
    include_package_data=True,
    packages=find_packages(),
    python_requires=">=2.7",
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
