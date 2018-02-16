"""
Hook to remove unused files.

See https://github.com/audreyr/cookiecutter/issues/723
"""

from os.path import join
import os
import shutil


def remove(filepath):
    """Remove file or directory."""
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)


if "{{cookiecutter.cli_type}}" == "click":
    remove(join("tests", "test_commands.py"))
    remove(join("{{cookiecutter.project_slug}}", "commands.py"))
