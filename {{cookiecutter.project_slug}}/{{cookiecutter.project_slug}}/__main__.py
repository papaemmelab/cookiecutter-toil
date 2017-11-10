"""
Entrypoint module, in case you use `python -m {{cookiecutter.project_slug}}`.

Why does this file exist, and why __main__? For more info, read:

- https://www.python.org/dev/peps/pep-0338/
- https://docs.python.org/3/using/cmdline.html#cmdoption-m
"""

from {{cookiecutter.project_slug}}.cli import main

if __name__ == "__main__":
    main()  # pylint: disable=no-value-for-parameter
