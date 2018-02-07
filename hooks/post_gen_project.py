"""
Hook to remove unused files.

See https://github.com/audreyr/cookiecutter/issues/723
"""

from os.path import join
import os
import shutil


def remove(filepath):
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)


if "{{cookiecutter.cli_type}}" == "click":
    for i in ["commands.py", "parsers.py", "jobs.py"]:
        remove(join("{{cookiecutter.project_slug}}", i))
        remove(join("tests", "test_" + i))
