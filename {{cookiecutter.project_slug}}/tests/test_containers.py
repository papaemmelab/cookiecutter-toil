"""{{cookiecutter.project_slug}} containers tests."""

from os.path import join
from os.path import abspath
from os.path import dirname
import os
import argparse
import subprocess

from docker.errors import APIError
import docker
import pytest
{% if cookiecutter.cli_type == "toil" %}
from toil.job import Job
from {{cookiecutter.project_slug}} import jobs
{% endif %}
from {{cookiecutter.project_slug}} import __version__
from {{cookiecutter.project_slug}} import singularity
from {{cookiecutter.project_slug}} import utils

ROOT = abspath(join(dirname(__file__), ".."))


@pytest.mark.skipif(
    not utils.is_docker_available(),
    reason="docker is not available."
    )
def test_docker_container():
    """
    Test the docker image is created properly and it executes the entrypoint
    as expected.

        docker build -t test-image .
        docker run -it test-image --version
    """
    # Get docker service from os environment
    client = docker.from_env()

    # Build image from Dockerfile
    docker_image = client.images.build(path=ROOT, rm=True)

    # Run detached container with command
    cmd_params = ['{{cookiecutter.project_slug}}', '--version']
    container = client.containers.run(docker_image, cmd_params, detach=True)
    container.stop()

    assert __version__ in container.logs().decode()


@pytest.mark.skipif(
    not utils.is_singularity_available(),
    reason="singularity is not available."
    )
def test_singularity_container():
    """
    Test the singularity image exists and its executable.

        singularity exec <test-image.simg> <command-parameters>
    """
    singularity_image = os.environ['TEST_SINGULARITY_IMAGE']
    cmd_parameters = ["cat", "/etc/os-release"]

    # Create call
    output = singularity.singularity_call(
        singularity_image,
        parameters=cmd_parameters,
        check_output=True
        )

    assert "VERSION" in output.decode()


{% if cookiecutter.cli_type == "toil" %}
# Toil Jobs and Options for testing
class ContainerizedCheckCallJob(jobs.BaseJob):
    """
    Job created to test that check_call is used correctly by docker
    and singularity.
    """
    cmd = ["pwd"]
    cwd = None
    env = {}

    def run(self, jobStore):
        """Saves a Hello message in a file."""
        return self.check_call(self.cmd, cwd=self.cwd, env=self.env)


class ContainerizedCheckOutputJob(jobs.BaseJob):
    """
    Job created to test that check_output is used correctly by docker
    and singularity.
    """
    cmd = ["pwd"]
    cwd = None
    env = {}

    def run(self, jobStore):
        """Saves a Hello message in a file."""
        return self.check_output(self.cmd, cwd=self.cwd, env=self.env)


def get_toil_test_parser():
    """Get test pipeline configuration using argparse."""
    # Add Toil options.
    parser = argparse.ArgumentParser()
    Job.Runner.addToilOptions(parser)

    # Parameters to run with docker or singularity
    settings = parser.add_argument_group("To run with docker or singularity:")

    settings.add_argument("--docker", default=False)
    settings.add_argument("--singularity", required=False)
    settings.add_argument("--shared-fs", required=False)

    return parser


@pytest.mark.skipif(
    not utils.is_singularity_available(),
    reason="singularity is not available."
    )
def test_singularity_toil(tmpdir):
    """
    Run a Toil job with the option --singularity SINGULARITY-IMAGE
    and --shared-fs SHARED-DIRECTORY to test the singularity wrapper
    is executing correctly the command inside the container.
    """
    # Create options for job
    workdir = join(str(tmpdir))
    jobstore = join(str(tmpdir), "jobstore")
    singularity_image = os.environ['TEST_SINGULARITY_IMAGE']
    shared_fs = os.environ['SHARED_FS']

    args = [
        jobstore,
        "--workDir", workdir,
        "--singularity", singularity_image,
        "--shared-fs", shared_fs,
        ]
    parser = get_toil_test_parser()
    options = parser.parse_args(args)

    # Create jobs
    job_call = ContainerizedCheckCallJob(
        options=options,
        unitName="Check call pwd",
        )

    job_output = ContainerizedCheckOutputJob(
        options=options,
        unitName="Check output pwd",
        )

    # Make sure that cwd functionality in check_output works
    job_output.cwd = "/home"
    std_output = job_output.run(jobstore)
    assert "/home" in std_output

    # Make sure that cwd functionality in check_call works
    std_call = job_call.run(jobstore)
    assert 0 == std_call

    # Make sure workDir is used as the tmp directory inside the container
    # and that an ENV variable is passed to the container system call.
    message = "Hello World"
    job_output.env = { "ISLAND": message}

    tmp_file = join("tmp", "bottle.txt")
    tmp_file_in_workdir = join(workdir, tmp_file)
    tmp_file_in_container = join(os.sep, tmp_file)

    job_output.cmd = [
        "/bin/bash",
        "-c",
        'echo $ISLAND > {}'.format(tmp_file_in_container)
        ]
    job_output.run(jobstore)

    with open(tmp_file_in_workdir) as f:
        assert message in f.read()


@pytest.mark.skipif(
    not utils.is_docker_available(),
    reason="docker is not available."
    )
def test_docker_toil(tmpdir):
    """
    Run a Toil job with the option flag --docker and --shared-fs
    SHARED-DIRECTORY to test the singularity wrapper is executing
    correctly the command inside the container.
    """
    # Create options for job
    workdir = join(str(tmpdir))
    jobstore = join(str(tmpdir), "jobstore")
    shared_fs = os.environ['SHARED_FS']

    # Clean images and build new image from Dockerfile
    client = docker.from_env()

    image_tag = 'test-toil'
    client.images.build(path=ROOT, rm=True, tag=image_tag)

    args = [
        jobstore,
        "--workDir", workdir,
        "--docker", image_tag,
        "--shared-fs", shared_fs,
    ]
    parser = get_toil_test_parser()
    options = parser.parse_args(args)

    # Create jobs
    job_call = ContainerizedCheckCallJob(
        options=options,
        unitName="Check call pwd",
        )
    job_output = ContainerizedCheckOutputJob(
        options=options,
        unitName="Check output pwd",
        )

    # Make sure that cwd functionality in check_output works
    job_output.cwd = "/home"
    std_output = job_output.run(jobstore)
    assert "/home" in std_output

    # Make sure that cwd functionality in check_call works
    std_call = job_call.run(jobstore)
    assert 0 == std_call

    # Make sure workDir is used as the tmp directory inside the container
    # and that an ENV variable is passed to the container system call.
    message = "Hello World"
    out_file = "bottle.txt"
    job_output.env = { "ISLAND": message}

    tmp_file_in_workdir = join(workdir, out_file)
    tmp_file_in_container = join(os.sep, "tmp", out_file)

    job_output.cmd = [
        "/bin/bash",
        "-c",
        'echo $ISLAND > {}'.format(tmp_file_in_container)
        ]
    job_output.run(jobstore)

    with open(tmp_file_in_workdir) as f:
        assert message in f.read()

{% endif %}
