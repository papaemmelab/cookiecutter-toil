# cookiecutter-toil

[![pypi badge][pypi_badge]][pypi_base]
[![travis badge][travis_badge]][travis_base]
[![pyup badge][pyup_badge]][pyup_base]
[![codecov badge][codecov_badge]][codecov_base]

A [cookiecutter] for the creation of [toil] and [click] Command Line Interfaces (CLI).

    # Run:
    cookiecutter https://github.com/leukgen/cookiecutter-toil

    # Or for ssh:
    cookiecutter git@github.com:leukgen/cookiecutter-toil.git

# Features

* 🐳 &nbsp; **Containerized System Calls**

    The `commands.BaseJob` inherits from [`toil_container.ContainerCallJob`][toil_container], a Job class with two abstract methods `check_output` and ``check_call`` that will be executed with either Docker, Singularity or Python's subprocess. See `toil_container` [README][toil_container] to learn more.

    A `Dockerfile` example is included. If you use [singularity], the generated `README` will include information on how to generate a singularity image.

* 📦 &nbsp; **Pip Installable!**

    Check the `setup.py` and `setup.json` for pip configurations. The only place where you have to define the **version** of your project is in the `setup.json` file. After generated, your project can be installed with:

        # local install
        pip install --editable <your_project_dir>

        # after deployment - check the continuous integration section
        pip install <your_project_name>

* 🍉 &nbsp; **Python Modules**

    | Module          | Description                                                                           |
    | --------------- | ------------------------------------------------------------------------------------- |
    | `cli.py`        | Include the function that is mapped to the cli command, see `setup.json:entry_points` |
    | `commands.py`   | Include a [toil] example pipeline                                                     |
    | `exceptions.py` | Include package specific exceptions                                                   |
    | `utils.py`      | Multiple util functions are available                                                 |
    | `validators.py` | Defines common validators                                                             |

* 🚧 &nbsp; **Contributing Features**

    | File              | Description                                                                    |
    | ----------------- | ------------------------------------------------------------------------------ |
    | `README.md`       | with some example sections.                                                    |
    | `CONTRIBUTING.md` | with full steps on how to properly contribute with your project.               |
    | `.gitignore`      | with well curated python ignore patterns.                                      |
    | `.gitmessage`     | with issue types mapped to emojis! Like 🚀 for a new feature, or 🐛 for a fix  |


* ✅ &nbsp; **Testing Suite**

    **Python** Some test examples are included using [pytest], give them a try with:

        py.test tests

    **Linting** Google style linting configuration is included in a [pylint] configuration file `.pylintrc`. Docstrings conventions to be tested with [pydocstyle] and are defined in `.pydocstylerc`.

        # check linting conventions
        pylint --rcfile={your_project_dir}/.pylintrc {your_project}

        # check docstrings
        pydocstyle --config={your_project_dir}/.pydocstylerc {your_project}

    **Full Picture** A [tox] setup is provided to run tests on isolated python environments. The `tox.ini` file enables you to run `pytest`, `pylint`, `pydocstyle` and [coverage]. Tox will also tests the installation procedure. To skip the installation, use `tox --develop` (great for development).

        # run the default tox environments
        tox

        # skip the installation, great for development
        tox --develop

        # run a subset of the environments
        tox -e report,lint

* 🌀 &nbsp; **Continuous Integration**

    [Travis CI] configuration with automatic deployment to `PyPi` with tags on `master`. To encrypt your `PyPi` password replace the field `deploy.password` in the `.travis.yml` configuration file and run:

        travis encrypt --add deploy.password

    Check out this [tutorial][travis_deploy] if you want to learn more about deployment.

* 🐁 &nbsp; **Click Mode**

    [Click] is an great package to seamlessly build CLI packages. Use `cli_type="click"` if you want to use the goodies of this cookiecutter but don't need the [toil] rocketry. By using this mode, some of the toil specific modules and tests will be removed.

# Contributing

Please see the [CONTRIBUTING.md](CONTRIBUTING.md) in this repository!

<!-- References -->
[singularity]: http://singularity.lbl.gov/
[toil_container]: https://github.com/leukgen/toil_container
[cookiecutter]: https://github.com/audreyr/cookiecutter
[toil]: http://toil.readthedocs.io/
[click]: http://click.pocoo.org/6/
[pytest]: https://docs.pytest.org/en/latest/
[pytest-env]: https://github.com/MobileDynasty/pytest-env
[tox]: http://tox.readthedocs.io/
[pydocstyle]: http://www.pydocstyle.org/en
[pylint]: https://www.pylint.org/
[coverage]: https://coverage.readthedocs.io
[travis ci]: https://travis-ci.org/
[travis_deploy]: https://docs.travis-ci.com/user/deployment/pypi/

<!-- Badges -->
[codecov_badge]: https://codecov.io/gh/leukgen/cookiecutter-toil/branch/master/graph/badge.svg
[codecov_base]: https://codecov.io/gh/leukgen/cookiecutter-toil
[pypi_badge]: https://img.shields.io/pypi/v/cookiecutter-toil.svg
[pypi_base]: https://pypi.python.org/pypi/cookiecutter-toil
[pyup_badge]: https://pyup.io/repos/github/leukgen/cookiecutter-toil/shield.svg
[pyup_base]: https://pyup.io/repos/github/leukgen/cookiecutter-toil/
[travis_badge]: https://img.shields.io/travis/leukgen/cookiecutter-toil.svg
[travis_base]: https://travis-ci.org/leukgen/cookiecutter-toil
