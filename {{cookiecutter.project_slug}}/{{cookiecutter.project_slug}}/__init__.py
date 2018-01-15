"""{{cookiecutter.project_slug}} module."""

import json
import os

ROOT = os.path.abspath(os.path.dirname(__file__))

try:
    # When locally installed.
    with open(os.path.join(ROOT, "..", "setup.json"), "r") as f:
        SETUP = json.load(f)

except IOError:
    # When not locally installed.
    with open(os.path.join(ROOT, "setup.json"), "r") as f:
        SETUP = json.load(f)

__version__ = SETUP.get("version")

__author__ = SETUP.get("author")
