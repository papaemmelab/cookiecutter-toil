"""cookiecutter-toil setup.py."""

from os.path import join
from os.path import abspath
from os.path import dirname
import io
import json

from setuptools import find_packages
from setuptools import setup


def read(path, **kwargs):
    """Return content of a file."""
    return io.open(path, encoding=kwargs.get("encoding", "utf8")).read()


ROOT = abspath(dirname(__file__))

# please put setup keywords in the setup.json to keep this file clean
with open(join(ROOT, "setup.json"), "r") as f:
    SETUP = json.load(f)

setup(
    # load description from README
    long_description=read(join(ROOT, "README.md")),

    # the version is only defined in one place
    version="0.1.0",

    # in combination with recursive-includes in MANIFEST.in, non-python files
    # included inside the {{cookiecutter.project_slug}} will be copied to the
    # site-packages installation directory
    include_package_data=True,

    # return a list all Python packages found within the ROOT directory
    packages=find_packages(),

    # pass parameters loaded from setup.json including author and version
    **SETUP
    )
