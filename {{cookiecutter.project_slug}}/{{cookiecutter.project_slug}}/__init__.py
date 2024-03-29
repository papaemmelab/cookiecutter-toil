"""{{cookiecutter.project_slug}} module."""

from os.path import abspath
from os.path import dirname
from os.path import join

# make sure we use absolute paths
ROOT = abspath(dirname(__file__))

with open(join(ROOT, "VERSION"), "r", encoding="utf-8") as f:
    VERSION = f.read().strip()

__version__ = VERSION
