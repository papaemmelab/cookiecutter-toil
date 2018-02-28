# {{cookiecutter.project_slug}}

[![pypi badge][pypi_badge]][pypi_base]
[![travis badge][travis_badge]][travis_base]
[![codecov badge][codecov_badge]][codecov_base]

{{cookiecutter.project_description}}

## Features

* 📦 &nbsp; **Easy Installation**

        pip install {{cookiecutter.project_slug}}

* 🍉 &nbsp; **Usage Documentation**

        {{cookiecutter.project_slug}} --help

* 🐳 &nbsp; **Containers Support**

        {% if cookiecutter.cli_type == "toil" %}{{cookiecutter.project_slug}}
            --volumes <local path> <container path>
            --docker {or --singularity} <image path or name>
            jobstore
        {% elif cookiecutter.cli_type == "click" %}# docker usage
        docker run --volume /shared_fs:/shared_fs --interactive --tty \
            {{cookiecutter.project_slug}}-image
            [{{cookiecutter.project_slug}} options]

        # singularity usage
        singularity run --workdir /shared_fs/tmp --bind /shared_fs:/shared_fs \
            {{cookiecutter.project_slug}}-singularity-image-path
            [{{cookiecutter.project_slug}} options]{% endif %}

    If you need to use [singularity], check [docker2singularity], and use `-m '/shared-fs-path /shared-fs-path'` to make sure your shared file system is mounted inside the singularity image.

## Contributing

Contributions are welcome, and they are greatly appreciated, check our [contributing guidelines](CONTROBUTING.md)!

## Credits

This package was created using [Cookiecutter] and the
[leukgen/cookiecutter-toil] project template.

<!-- References -->
[singularity]: http://singularity.lbl.gov/
[docker2singularity]: https://github.com/singularityware/docker2singularity
[cookiecutter]: https://github.com/audreyr/cookiecutter
[leukgen/cookiecutter-toil]: https://github.com/leukgen/cookiecutter-toil

<!-- Badges -->
[codecov_badge]: https://codecov.io/gh/{{cookiecutter.github_account}}/{{cookiecutter.project_slug}}/branch/master/graph/badge.svg
[codecov_base]: https://codecov.io/gh/{{cookiecutter.github_account}}/{{cookiecutter.project_slug}}
[pypi_badge]: https://img.shields.io/pypi/v/{{cookiecutter.project_slug}}.svg
[pypi_base]: https://pypi.python.org/pypi/{{cookiecutter.project_slug}}
[travis_badge]: https://img.shields.io/travis/{{cookiecutter.github_account}}/{{cookiecutter.project_slug}}.svg
[travis_base]: https://travis-ci.org/{{cookiecutter.github_account}}/{{cookiecutter.project_slug}}
