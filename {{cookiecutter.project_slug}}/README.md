# {{cookiecutter.project_slug}}

Please just use this readme for docs.

# Contents

- [{{cookiecutter.project_slug}}](#cookiecutterprojectslug)
- [Contents](#contents)
- [Usage](#usage)
- [Installation](#installation)
- [Docker](#docker)
- [Singularity](#singularity)

# Usage

Example...

# Installation

Example...

    pip install --editable .


# Docker

Local directories can be mounted in the container using the `--volume` flag. (please note it doesn't need to be `/shared_fs`, it could be `/ifs`).

    # build the image
    docker build --tag {{cookiecutter.project_slug}}-image .

    # run the container
    {% if cookiecutter.cli_type == "click" %}
    docker run \
        --volume /shared_fs:/shared_fs                  \ # bind the local /shared_fs to the /shared_fs container
        --interactive                                   \ # Keep STDIN open even if not attached
        --tty                                           \ # Allocate a pseudo-TTY
        {{cookiecutter.project_slug}}-image             \ # The tag name of the image as defined in docker build
            [--{{cookiecutter.project_slug}}-options]

    {% elif cookiecutter.cli_type == "toil" %}
    {{cookiecutter.project_slug}}
        [--toil-options]
        [--{{cookiecutter.project_slug}}-options]
        --docker {{cookiecutter.project_slug}}-image
        --shared-fs /shared_fs
    {% endif %}

# Singularity

Once created the docker image, run `singularityware/docker2singularity` to create the singularity image. If you are running in a shared file system (e.g. `/shared_fs`), you can mount this directory in the container by using the `-m` flag (multiple `-m` are allowed):

    # build the image
    docker build --tag {{cookiecutter.project_slug}}-image .

    # this command must be run in a local machine with docker❗️
    docker run \
        -v /var/run/docker.sock:/var/run/docker.sock \
        -v `pwd`:/output \
        --privileged -t --rm \
        singularityware/docker2singularity \
        -m '/shared_fs /shared_fs'
        {{cookiecutter.project_slug}}-image

The previous command will create a singularity image named with `$creation_date` and `$container_id` variables. These will be unique to each run of `singularityware/docker2singularity`

    # set the path to the singularity image
    SIGULARITY_IMAGE_PATH=`pwd`/{{cookiecutter.project_slug}}-image-$creation_date-$container_id.img

    # run the container
    {% if cookiecutter.cli_type == "click" %}
    singularity run \
        --workdir /shared_fs/tmp      \ # Working directory to be used for /tmp, /var/tmp and $HOME
        --bind /shared_fs:/shared_fs  \ # /shared_fs mount point made available by using -m in docker2singularity
        $SIGULARITY_IMAGE_PATH
            [--{{cookiecutter.project_slug}}-options]

    {% elif cookiecutter.cli_type == "toil" %}
    {{cookiecutter.project_slug}}
        [--toil-options]
        [--{{cookiecutter.project_slug}}-options]
        --docker {{cookiecutter.project_slug}}-image
        --shared-fs /shared_fs
    {% endif %}
