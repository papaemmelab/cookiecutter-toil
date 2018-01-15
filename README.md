# cookiecutter-cli

Cookiecutter template for toil/click based Command Line Interfaces (CLI).

    # Run:
    cookiecutter https://github.com/leukgen/cookiecutter-cli

    # Or for ssh:
    cookiecutter git@github.com:leukgen/cookiecutter-cli.git


# Table of Contents

<!-- This is for SublimeText's MarkdownTOC -->
<!-- MarkdownTOC autolink="true" bracket="round" depth=2 -->

- [Features](#features)
    - [Toil](#toil)
    - [Click](#click)
    - [Testing](#testing)
    - [Modules](#modules)
    - [Installation](#installation)
    - [Docker](#docker)
    - [Contributing](#contributing)

<!-- /MarkdownTOC -->

# Features

This [cookiecutter][cookiecutter] enables the creation of [toil][toil] and [click][click] CLI tools.

## Toil

When running with the `toil` option, an example pipeline will be generated. Examples of how to run both holistic and unit tests for [toil][toil] pipelines are included. This cookiecutter suggests the following design pattern:

- 1. `get_parser`: this function builds an `arg_parse` object that includes both toil options and pipeline specific options. These will be separated in different sections of the `--help` text.
- 2. `process_parsed_options`: once the options are parsed, it maybe necessary to conduct *post-parsing* operations such as adding new attributes to the `options` namespace or validating combined arguments.
- 3. `run_toil`: this function uses the `options` namespace to build and run the toil `DAG`.

## Click

[Click][click] is an amazing package to seamlessly build CLI packages. We included a simple hello world example.

## Testing

The generated projects come with an initial test suite ready to be run using [pytest][pytest]. Check the `CONTRIBUTING.md` file included in the project to explore the testing steps. A `pytest.ini` is included and can be used to define test specific configuration variables using [pytest-env][pytest-env]. Check it out with the following command:

    py.test tests

A `.coveragerc` configuration file is generated. To get coverage statistics run:

    py.test tests --cov={your_project_dir}

Additionally, a `.pylintrc` is provided with world-class style configuration:

    pylint {your_project} --rcfile={your_project_dir}/.pylintrc

To run more comprehensive tests, a `tox.ini` file is included. Out of the box, this configuration enables you to get `pytest`, `pylint` and a coverage html report. Tox also tests the installation procedure, which at the moment is set for python 2.7. Check the configuration file to learn more or run:

    tox

## Modules

The following modules will be included in the generated program (all modules come with tests):

| Module        | Description                                                                           |
|---------------|---------------------------------------------------------------------------------------|
| cli.py        | Include the function that is mapped to the cli command, see `setup.json:entry_points` |
| commands.py   | Include example pipelines for both [toil][toil] and [click][click]                    |
| exceptions.py | Include package specific exceptions                                                   |
| utils.py      | Multiple util functions are available                                                 |
| validators.py | Defines common validators                                                             |

## Installation

Your project will be pip installable! Check the `setup.py` and `setup.json` for pip configurations. To install, run:

    pip install --editable {your_project_dir}

The only place where you have to define the version of your project is in the `setup.json` file. The `MANIFEST.in` file defines the files that should be included in the pip installation directory.

## Docker

A docker directory is included with an example `Dockerfile`.

## Contributing

Your project will also come with the following contributing tools:

- 1. `README.md` with some example sections.
- 2. `CONTRIBUTING.md` with full steps on how to properly contribute with your project.
- 3. `.gitignore` with well curated python ignore patterns.
- 4. `.gitmessage` with issue types mapped to emojis! Like :fire: for a new feature, or :bug: for a fix.

<!-- References -->

[cookiecutter]: https://github.com/audreyr/cookiecutter
[toil]: http://toil.readthedocs.io/
[click]: http://click.pocoo.org/6/
[pytest]: https://docs.pytest.org/en/latest/
[pytest-env]: https://github.com/MobileDynasty/pytest-env
