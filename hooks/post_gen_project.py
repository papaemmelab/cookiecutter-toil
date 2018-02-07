"""
Hook to remove unused files.

See https://github.com/audreyr/cookiecutter/issues/723
"""

import os
import shutil


def remove(filepath):
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)


if "{{cookiecutter.cli_type}}" == "click":
    remove(os.path.join("{{cookiecutter.project_slug}}", "commands.py"))
    remove(os.path.join("{{cookiecutter.project_slug}}", "parsers.py"))
    remove(os.path.join("{{cookiecutter.project_slug}}", "jobs.py"))
