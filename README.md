# cookiecutter-cli

This [cookiecutter][cookiecutter] enables the creation of [toil][toil] and [click][click] Command Line Interfaces (CLI).

    # Run:
    cookiecutter https://github.com/leukgen/cookiecutter-cli

    # Or for ssh:
    cookiecutter git@github.com:leukgen/cookiecutter-cli.git

# Contents

- [cookiecutter-cli](#cookiecutter-cli)
- [Contents](#contents)
- [Features](#features)
    - [Container Calls](#container-calls)
    - [Custom Toil Parser](#custom-toil-parser)
    - [Docker and Singularity Support](#docker-and-singularity-support)
    - [Python Modules](#python-modules)
    - [Contributing Features](#contributing-features)
    - [Click Mode](#click-mode)
    - [Pip Installable](#pip-installable)
    - [Testing Suite](#testing-suite)
        - [Pytest](#pytest)
        - [Linting](#linting)
        - [Tox](#tox)
- [Contributing To This Cookiecutter](#contributing-to-this-cookiecutter)


# Features

This [cookiecutter][cookiecutter] enables the creation of [toil][toil] CLI tools. Check the following features 🚀

## Container Calls

A custom `BaseJob` that inherits from `toil.jobs.Job` is available. This class has two special methods `check_call` and `check_output`. These will perform system calls using `docker`, `singularity` or `subprocess` depending on availability.

## Custom Toil Parser

Sometimes all the `toil` options may scare your users. This `cookiecutter` has a custom parser that by default only includes the required toil arguments in the `help` print. Additionally, it includes a `container arguments` section that can be toggled off. Check it out:


    usage: your_tool [-h] [-v] [--help-toil] [--docker DOCKER-IMAGE-NAME]
                [--singularity SINGULARITY-IMAGE-PATH] [--shared-fs SHARED_FS]
                [TOIL EXTRA ARGS]
                jobStore

    optional arguments:
    -h, --help            show this help message and exit
    -v, --version         show program's version number and exit
    --help-toil           print help with full list of Toil arguments and exit

    container arguments:
    --docker DOCKER-IMAGE-NAME
                            name of the docker image, available in daemon
    --singularity SINGULARITY-IMAGE-PATH
                            path of the singularity image (.simg) to jobs be run
                            inside singularity containers
    --shared-fs SHARED_FS
                            shared file system path to be mounted in containers

    toil arguments:
    TOIL EXTRA ARGS       see --help-toil for a full list of toil parameters
    jobStore              the location of the job store for the workflow. See
                            --help-toil for more information [REQUIRED]

## Docker and Singularity Support

A `Dockerfile` example is included. If you use [singularity][singularity], the generated `README` will include information on how to generate a singularity image.

## Python Modules

The following modules will be included in the generated program (all modules come with tests):

| Module        | Description                                                                           |
| ------------- | ------------------------------------------------------------------------------------- |
| cli.py        | Include the function that is mapped to the cli command, see `setup.json:entry_points` |
| commands.py   | Include a [toil][toil] example pipeline                                               |
| jobs.py       | A module to define toil jobs                                                          |
| exceptions.py | Include package specific exceptions                                                   |
| utils.py      | Multiple util functions are available                                                 |
| validators.py | Defines common validators                                                             |
| parsers.py    | Custom Argparse class with container and simplified toil options                      |

## Contributing Features

Your project will also come with the following contributing tools:

- 1. `README.md` with some example sections.
- 2. `CONTRIBUTING.md` with full steps on how to properly contribute with your project.
- 3. `.gitignore` with well curated python ignore patterns.
- 4. `.gitmessage` with issue types mapped to emojis! Like :fire: for a new feature, or :bug: for a fix.

## Click Mode

[Click][click] is an great package to seamlessly build CLI packages. Use `cli_mode="click"`  if you want to use the goodies of this cookiecutter but don't need the [toil][toil] rocketry. By using this mode, some of the toil specific modules and tests will be removed.

## Pip Installable

Your project will be pip installable! Check the `setup.py` and `setup.json` for pip configurations. To install, run:

    pip install --editable {your_project_dir}

The only place where you have to define the version of your project is in the `setup.json` file. The `MANIFEST.in` file defines the files that should be included in the pip installation directory.

## Testing Suite

### Pytest

The generated projects come with an initial test suite ready to be run using [pytest][pytest]. Check the `CONTRIBUTING.md` file included in the project to explore the testing steps. A `pytest.ini` is included and can be used to define test specific configuration variables using [pytest-env][pytest-env]. Check it out with the following command:

    py.test tests

A `.coveragerc` configuration file is generated. To get coverage statistics run:

    py.test tests --cov={your_project_dir}

### Linting

A `.pylintrc` is provided with world-class [pylint][pylint] configuration:

    pylint --rcfile={your_project_dir}/.pylintrc {your_project}

Additionally, a `.pydocstylerc` configuration is included with a set of *docstrings* conventions to be tested with [pydocstyle][pydocstyle].

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
