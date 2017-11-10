"""{{cookiecutter.project_slug}} setup.py."""

# python
import io
import json
import os

# third party
from setuptools import find_packages
from setuptools import setup

ROOT = os.path.abspath(os.path.dirname(__file__))


def read(path, **kwargs):
    """Return content of a file."""
    return io.open(path, encoding=kwargs.get("encoding", "utf8")).read()


# Please put setup keywords in the setup.json to keep this file clean.
with open(os.path.join(ROOT, "setup.json"), "r") as f:
    SETUP = json.load(f)

setup(
    long_description=read(os.path.join(ROOT, "README.md")),
    packages=find_packages(),
    **SETUP
    )
