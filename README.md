# cookiecutter-toil

[![pypi badge][pypi_badge]][pypi_base]
[![travis badge][travis_badge]][travis_base]
[![pyup badge][pyup_badge]][pyup_base]

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

    Check the `setup.py` and `setup.json` for pip configurations. The only place where you have to define the **version** of your project is in the [`VERSION`] file. After generated, your project can be installed with:

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

    | File                 | Description                                                                   |
    | -------------------- | ----------------------------------------------------------------------------- |
    | `README.md`          | with some example sections                                                    |
    | `CONTRIBUTING.md`    | with full steps on how to properly contribute with your project               |
    | `.gitignore`         | with well curated python ignore patterns                                      |
    | `.gitmessage`        | with issue types mapped to emojis! Like 🚀 for a new feature, or 🐛 for a fix |
    | `CODE_OF_CONDUCT.md` | A [covenant] code of conduct                                                  |


* ✅ &nbsp; **Testing Suite**

    **[Pytest]**: python test examples are included, give them a try with:

        py.test tests

    **[Pylint]**: Google style linting configuration is included with the `.pylintrc`. Additionally, Docstrings conventions are tested with [pydocstyle] and are defined in `.pydocstylerc`.

        # check linting conventions
        pylint --rcfile={your_project_dir}/.pylintrc {your_project}

        # check docstrings
        pydocstyle --config={your_project_dir}/.pydocstylerc {your_project}

    **[Tox]**: Run `pytest`, `pylint`, `pydocstyle` with [coverage] on isolated python environments at the same time:

        tox

* 🌀 &nbsp; **Continuous Integration**

    [Travis CI] configuration with automatic deployment to `PyPi` with tags on `master`. To encrypt your `PyPi` password replace the field `deploy.password` in the `.travis.yml` configuration file and run:

        travis encrypt --add deploy.password

    Check out this [tutorial][travis_deploy] if you want to learn more about deployment.

* 🐁 &nbsp; **Click Mode**

    [Click] is an great package to seamlessly build CLI packages. Use `cli_type="click"` if you want to use the goodies of this cookiecutter but don't need the [toil] rocketry. By using this mode, some of the toil specific modules and tests will be removed.

# Contributing

Please see the [CONTRIBUTING.md](CONTRIBUTING.md) in this repository!

<!-- References -->
[`VERSION`]: https://packaging.python.org/guides/single-sourcing-package-version/
[click]: http://click.pocoo.org/6/
[covenant]: http://contributor-covenant.org/version/1/4/
[cookiecutter]: https://github.com/audreyr/cookiecutter
[coverage]: https://coverage.readthedocs.io
[pydocstyle]: http://www.pydocstyle.org/en
[pylint]: https://www.pylint.org/
[pytest-env]: https://github.com/MobileDynasty/pytest-env
[pytest]: https://docs.pytest.org/en/latest/
[singularity]: http://singularity.lbl.gov/
[toil_container]: https://github.com/leukgen/toil_container
[toil]: http://toil.readthedocs.io/
[tox]: http://tox.readthedocs.io/
[travis ci]: https://travis-ci.org/
[travis_deploy]: https://docs.travis-ci.com/user/deployment/pypi/

<!-- Badges -->
[pypi_badge]: https://img.shields.io/pypi/v/cookiecutter-toil.svg
[pypi_base]: https://pypi.python.org/pypi/cookiecutter-toil
[pyup_badge]: https://pyup.io/repos/github/leukgen/cookiecutter-toil/shield.svg
[pyup_base]: https://pyup.io/repos/github/leukgen/cookiecutter-toil/
[travis_badge]: https://img.shields.io/travis/leukgen/cookiecutter-toil.svg
[travis_base]: https://travis-ci.org/leukgen/cookiecutter-toil
