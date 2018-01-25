# cookiecutter-cli

This [cookiecutter][cookiecutter] enables the creation of [toil][toil] and [click][click] Command Line Interfaces (CLI).

    # Run:
    cookiecutter https://github.com/leukgen/cookiecutter-cli

    # Or for ssh:
    cookiecutter git@github.com:leukgen/cookiecutter-cli.git

# Contents

- [cookiecutter-cli](#cookiecutter-cli)
- [Contents](#contents)
- [Modes](#modes)
    - [Toil - python 2.7](#toil---python-27)
    - [Click - python 3.6](#click---python-36)
- [Features](#features)
    - [Predefined Python Modules](#predefined-python-modules)
    - [Full Testing Suite](#full-testing-suite)
        - [Pytest](#pytest)
        - [Linting](#linting)
        - [Tox](#tox)
    - [Docker and Singularity Deployment](#docker-and-singularity-deployment)
    - [Pip Installable](#pip-installable)
    - [Contributing Features](#contributing-features)
- [Contributing To This Cookiecutter](#contributing-to-this-cookiecutter)


# Modes

This [cookiecutter][cookiecutter] enables the creation of [toil][toil] and [click][click] Command Line Interfaces (CLI).

## Toil - python 2.7

When running with the `toil` option, an example pipeline will be generated.Examples of how to run both holistic and unit tests for [toil][toil] pipelines are included. This cookiecutter suggests the following design pattern:

- 1. `get_parser`: this function builds an `arg_parse` object that includes both toil options and pipeline specific options. These will be separated in different sections of the `--help` text.

- 2. `process_parsed_options`: once the options are parsed, it maybe necessary to conduct *post-parsing* operations such as adding new attributes to the `options` namespace or validating combined arguments.

- 3. `run_toil`: this function uses the `options` namespace to build and run the toil `DAG`.

## Click - python 3.6

[Click][click] is an great package to seamlessly build CLI packages. We included a simple hello world example.

# Features

## Predefined Python Modules

The following modules will be included in the generated program (all modules come with tests):

| Module        | Description                                                                           |
| ------------- | ------------------------------------------------------------------------------------- |
| cli.py        | Include the function that is mapped to the cli command, see `setup.json:entry_points` |
| commands.py   | Include example pipelines for both [toil][toil] and [click][click]                    |
| exceptions.py | Include package specific exceptions                                                   |
| utils.py      | Multiple util functions are available                                                 |
| validators.py | Defines common validators                                                             |

## Full Testing Suite

### Pytest

The generated projects come with an initial test suite ready to be run using [pytest][pytest]. Check the `CONTRIBUTING.md` file included in the project to explore the testing steps. A `pytest.ini` is included and can be used to define test specific configuration variables using [pytest-env][pytest-env]. Check it out with the following command:

    py.test tests

A `.coveragerc` configuration file is generated. To get coverage statistics run:

    py.test tests --cov={your_project_dir}

### Linting

A `.pylintrc` is provided with world-class [pylint][pylint] configuration:

    pylint --rcfile={your_project_dir}/.pylintrc {your_project}

Additionally, a `.pydocstyle` configuration is included with a set of *docstrings* conventions to be tested with [pydocstyle][pydocstyle].

    pydocstyle --config={your_project_dir}/.pydocstylerc {your_project}

### Tox

Use [tox][tox] run tests on a isolated python environment. The `tox.ini` file enables you to get [pytest][pytest], [pylint][pylint], [pydocstyle][pydocstyle] and a [coverage][coverage] html report. Tox also tests the installation procedure. To execute the default environments run:

    tox

You can run a set of specific test environments:

    tox -e report,lint

The `report` enviroment will create a html coverage report. Use `tox --recreate` when you need to rebuild the tox environments (e.g. you changed one of the `deps` lists in the `tox.ini` file). The available tox environments are:

| Name   | function                                                                                          |
| ------ | ------------------------------------------------------------------------------------------------- |
| py27   | Test package using python 2                                                                       |
| py36   | Test package using python 3                                                                       |
| lint   | Run [pylint][pylint] and [pydocstyle][pydocstyle] using the `.pylintrc` and `.pydocstylerc` files |
| report | Run base tests and generate coverage statistics                                                   |
| clean  | Clean a previously generated coverage report                                                      |

## Docker and Singularity Deployment

A `Dockerfile` example is included. if you use [singularity], a `docker2singularity` script is available.

## Pip Installable

Your project will be pip installable! Check the `setup.py` and `setup.json` for pip configurations. To install, run:

    pip install --editable {your_project_dir}

The only place where you have to define the version of your project is in the `setup.json` file. The `MANIFEST.in` file defines the files that should be included in the pip installation directory.

## Contributing Features

Your project will also come with the following contributing tools:

- 1. `README.md` with some example sections.
- 2. `CONTRIBUTING.md` with full steps on how to properly contribute with your project.
- 3. `.gitignore` with well curated python ignore patterns.
- 4. `.gitmessage` with issue types mapped to emojis! Like :fire: for a new feature, or :bug: for a fix.

# Contributing To This Cookiecutter

Please see the `CONTRIBUTING.md` in this repository!

<!-- References -->

[cookiecutter]: https://github.com/audreyr/cookiecutter
[toil]: http://toil.readthedocs.io/
[click]: http://click.pocoo.org/6/
[pytest]: https://docs.pytest.org/en/latest/
[pytest-env]: https://github.com/MobileDynasty/pytest-env
[tox]: http://tox.readthedocs.io/
[pydocstyle]: http://www.pydocstyle.org/en
[pylint]: https://www.pylint.org/
[coverage]:https://coverage.readthedocs.io
