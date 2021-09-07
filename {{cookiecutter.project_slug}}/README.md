# {{cookiecutter.project_slug}}

[![pypi badge][pypi_badge]][pypi_base]
[![travis badge][travis_badge]][travis_base]
[![codecov badge][codecov_badge]][codecov_base]
[![docker badge][docker_badge]][docker_base]
[![docker badge][automated_badge]][docker_base]
[![code formatting][black_badge]][black_base]

{{cookiecutter.project_description}}

## Usage

{% if cookiecutter.cli_type == "toil" %}This package uses docker to manage its dependencies, there are 2 ways of using it:

1. Running the [container][docker_base] in single machine mode without [`--batchSystem`] support:

        # using docker
        docker run -it {{cookiecutter.github_account}}/{{cookiecutter.project_slug}} --help

        # using singularity
        singularity run docker://{{cookiecutter.github_account}}/{{cookiecutter.project_slug}} --help

1. Installing the python package from [pypi][pypi_base] and passing the container as a flag:

        # install package
        pip install {{cookiecutter.project_slug}}

        # run with docker
        {{cookiecutter.project_slug}} [TOIL-OPTIONS] [PIPELINE-OPTIONS]
            --docker {{cookiecutter.github_account}}/{{cookiecutter.project_slug}}
            --volumes <local path> <container path>
            --batchSystem LSF

        # run with singularity
        {{cookiecutter.project_slug}} [TOIL-OPTIONS] [PIPELINE-OPTIONS]
            --singularity docker://{{cookiecutter.github_account}}/{{cookiecutter.project_slug}}
            --volumes <local path> <container path>
            --batchSystem LSF{% elif cookiecutter.cli_type == "click" %}Run with [containers][docker_base]:

        # docker usage
        docker run {{cookiecutter.github_account}}/{{cookiecutter.project_slug}} --help

        # singularity usage
        singularity run docker://{{cookiecutter.github_account}}/{{cookiecutter.project_slug}} --help
{% endif %}
See [docker2singularity] if you want to use a [singularity] image instead of using the `docker://` prefix.

## Contributing

Contributions are welcome, and they are greatly appreciated, check our [contributing guidelines](.github/CONTRIBUTING.md)!

## Credits

This package was created using [Cookiecutter] and the
[papaemmelab/cookiecutter-toil] project template.

[`--batchSystem`]: http://toil.readthedocs.io/en/latest/developingWorkflows/batchSystem.html?highlight=BatchSystem
[automated_badge]: https://img.shields.io/docker/cloud/automated/{{cookiecutter.github_account}}/{{cookiecutter.project_slug}}.svg
[black_badge]: https://img.shields.io/badge/code%20style-black-000000.svg
[black_base]: https://github.com/ambv/black
[codecov_badge]: https://codecov.io/gh/{{cookiecutter.github_account}}/{{cookiecutter.project_slug}}/branch/master/graph/badge.svg
[codecov_base]: https://codecov.io/gh/{{cookiecutter.github_account}}/{{cookiecutter.project_slug}}
[cookiecutter]: https://github.com/audreyr/cookiecutter
[docker_badge]: https://img.shields.io/docker/cloud/build/{{cookiecutter.github_account}}/{{cookiecutter.project_slug}}.svg
[docker_base]: https://hub.docker.com/r/{{cookiecutter.github_account}}/{{cookiecutter.project_slug}}
[docker2singularity]: https://github.com/singularityware/docker2singularity
[papaemmelab/cookiecutter-toil]: https://github.com/papaemmelab/cookiecutter-toil
[pypi_badge]: https://img.shields.io/pypi/v/{{cookiecutter.project_slug}}.svg
[pypi_base]: https://pypi.python.org/pypi/{{cookiecutter.project_slug}}
[singularity]: http://singularity.lbl.gov/
[travis_badge]: https://img.shields.io/travis/{{cookiecutter.github_account}}/{{cookiecutter.project_slug}}.svg
[travis_base]: https://travis-ci.com/{{cookiecutter.github_account}}/{{cookiecutter.project_slug}}
