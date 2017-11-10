"""{{cookiecutter.project_slug}} module."""

# python
import json
import os

ROOT = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(ROOT, "..", "setup.json"), "r") as f:
    SETUP = json.load(f)

__version__ = SETUP.get("version")

__author__ = SETUP.get("author")
