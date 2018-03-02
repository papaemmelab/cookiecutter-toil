# cookiecutter-toil

[![pypi badge][pypi_badge]][pypi_base]
[![gitter badge][gitter_badge]][gitter_base]
[![travis badge][travis_badge]][travis_base]
[![pyup badge][pyup_badge]][pyup_base]

A [cookiecutter] for the creation of [toil] pipelines.

    pip install cookiecutter-toil
    cookiecutter cookiecutter-toil

## Live Example

[![travis badge][example_travis_badge]][example_travis_base]
[![codecov badge][example_codecov_badge]][example_codecov_base]

Check out [toil_example], this project is updated automatically with every new commit on cookiecutter-toil.

## Features

* 🐳 &nbsp; **Containerized System Calls**

    The `commands.BaseJob` inherits from [`ContainerJob`][toil_container], a Job Class used to run commands with either Docker, Singularity or Python's subprocess. See [toil_container] to learn more.

    A `Dockerfile` example is included. If you use [singularity], the generated `README` will include information on how to generate a singularity image.

* 📦 &nbsp; **Pip Installable Project**

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

    | File          | Description                                                                   |
    | ------------- | ----------------------------------------------------------------------------- |
    | `README.md`   | with some example sections                                                    |
    | `.gitignore`  | with well curated python ignore patterns                                      |
    | `.gitmessage` | with issue types mapped to emojis! Like 🚀 for a new feature, or 🐛 for a fix |
    | `.github`     | Contributing guidelines, code of conduct, issue and PR templates              |

* ✅ &nbsp; **Testing Suite**

    **[Pytest]**: python test examples are included, give them a try with:

        py.test tests

    **[Pylint]**: Google style linting configuration is included with the [`.pylintrc`]. Additionally, Docstrings conventions are tested with [pydocstyle] and are defined in [`.pydocstylerc`].

        # check linting conventions
        pylint --rcfile={your_project_dir}/.pylintrc {your_project}

        # check docstrings
        pydocstyle --config={your_project_dir}/.pydocstylerc {your_project}

    **[Tox]**: Run `pytest`, `pylint`, `pydocstyle` with [coverage] on isolated python environments at the same time:

        tox

* 🌀 &nbsp; **Continuous Integration**

    [Travis CI] configuration with automatic deployment to `PyPi` with tags on `master`. To encrypt your `PyPi` password simply run:

        # you need travis (e.g. brew install travis)
        travis encrypt --add deploy.password

    Check out this [tutorial][travis_deploy] if you want to learn more about deployment.

* 🐁 &nbsp; **Click Mode**

    [Click] is an great package to seamlessly build CLI packages. Use `cli_type="click"` if you want to use the goodies of this cookiecutter but don't need the [toil] rocketry. By using this mode, some of the toil specific modules and tests will be removed.

## Contributing

Please see the [CONTRIBUTING.md](.github/CONTRIBUTING.md) in this repository!

<!-- References -->
[`.pydocstylerc`]: {{cookiecutter.project_slug}}/.pydocstylerc
[`.pylintrc`]: {{cookiecutter.project_slug}}/.pylintrc
[`VERSION`]: https://packaging.python.org/guides/single-sourcing-package-version/
[click]: http://click.pocoo.org/6/
[cookiecutter]: https://github.com/audreyr/cookiecutter
[covenant]: http://contributor-covenant.org/version/1/4/
[coverage]: https://coverage.readthedocs.io
[pydocstyle]: http://www.pydocstyle.org/en
[pylint]: https://www.pylint.org/
[pytest-env]: https://github.com/MobileDynasty/pytest-env
[pytest]: https://docs.pytest.org/en/latest/
[singularity]: http://singularity.lbl.gov/
[toil_container]: https://github.com/leukgen/toil_container
[toil_example]: https://github.com/leukgen/toil_example
[toil]: http://toil.readthedocs.io/
[tox]: http://tox.readthedocs.io/
[travis ci]: https://travis-ci.org/
[travis_deploy]: https://docs.travis-ci.com/user/deployment/pypi/

<!-- Badges -->
[gitter_badge]: https://badges.gitter.im/leukgen/cookiecutter-toil/Lobby.svg
[gitter_base]: https://gitter.im/leukgen/cookiecutter-toil
[pypi_badge]: https://img.shields.io/pypi/v/cookiecutter-toil.svg
[pypi_base]: https://pypi.python.org/pypi/cookiecutter-toil
[pyup_badge]: https://pyup.io/repos/github/leukgen/cookiecutter-toil/shield.svg
[pyup_base]: https://pyup.io/repos/github/leukgen/cookiecutter-toil/
[travis_badge]: https://img.shields.io/travis/leukgen/cookiecutter-toil.svg
[travis_base]: https://travis-ci.org/leukgen/cookiecutter-toil

<!-- toil example badges -->
[example_codecov_badge]: https://codecov.io/gh/leukgen/toil_example/branch/master/graph/badge.svg
[example_codecov_base]: https://codecov.io/gh/leukgen/toil_example
[example_travis_badge]: https://img.shields.io/travis/leukgen/toil_example.svg
[example_travis_base]: https://travis-ci.org/leukgen/toil_example
