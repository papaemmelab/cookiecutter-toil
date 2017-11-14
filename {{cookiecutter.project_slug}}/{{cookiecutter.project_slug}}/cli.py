"""
Module that contains the command line app.

Why does this file exist, and why not put this in __main__?
You might be tempted to import things from __main__ later, but that will
cause problems, the code will get executed twice:

    - When you run `python -m {{cookiecutter.project_slug}}` python will execute
      `__main__.py` as a script. That means there won't be any
      `{{cookiecutter.project_slug}}.__main__` in `sys.modules`.

    - When you import __main__ it will get executed again (as a module) because
      there's no `{{cookiecutter.project_slug}}.__main__` in `sys.modules`.

Also see (1) from http://click.pocoo.org/5/setuptools/#setuptools-integration
"""

# local
from {{cookiecutter.project_slug}} import jobs


def main():
    """{{cookiecutter.project_slug}} main command."""
    jobs.run_pipeline()
