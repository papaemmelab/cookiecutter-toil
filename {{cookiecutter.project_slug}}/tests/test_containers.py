"""{{cookiecutter.project_slug}} containers tests."""

from os.path import join
from os.path import abspath
from os.path import dirname
import os
import argparse
import subprocess

{% if cookiecutter.cli_type == "toil" %}from toil.job import Job{% endif %}
from docker.errors import APIError
import docker
import pytest

from {{cookiecutter.project_slug}} import __version__
from {{cookiecutter.project_slug}} import jobs
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
    cmd_params = ['--version']
    container = client.containers.run(docker_image, cmd_params, detach=True)
    expected_stdout = "{main_cmd} {version}".format(
        main_cmd="{{cookiecutter.project_slug}}",
        version=__version__
        )
    container.stop()

    assert expected_stdout in container.logs()


@pytest.mark.skipif(
    not utils.is_singularity_available(),
    reason="singularity is not available."
    )
def test_singularity_container():
    """
    Test the singularity image exists and its executable.

        singularity exec <test-image.simg> <command-parameters>
    """
    singularity_image = os.environ['TEST_CONTAINER_IMAGE']
    cmd_parameters = ["cat", "/etc/os-release"]

    # Create call
    output = singularity.singularity_call(
        singularity_image,
        parameters=cmd_parameters,
        check_output=True
        )

    assert 'VERSION' in output


{% if cookiecutter.cli_type == "toil" %}
# Toil Jobs and Options for testing
class ContainerizedCheckCallJob(jobs.BaseJob):
    """
    Job created to test that check_call is used correctly by docker
    and singularity.
    """
    def run(self, jobStore):
        """Saves a Hello message in a file."""
        cmd = ["cat", "/etc/os-release"]
        return self.check_call(cmd, cwd=self.options.workDir)


class ContainerizedCheckOutputJob(jobs.BaseJob):
    """
    Job created to test that check_output is used correctly by docker
    and singularity.
    """

    def run(self, jobStore):
        """Saves a Hello message in a file."""
        cmd = ["echo", "$TMP"]
        return self.check_output(cmd, cwd=self.options.workDir)


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
    singularity_image = os.environ['TEST_CONTAINER_IMAGE']
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
        unitName="Hello World",
        )
    job_output = ContainerizedCheckOutputJob(
        options=options,
        unitName="Hello World",
        )

    # Run jobs
    std_call = job_call.run(jobstore)
    std_output = job_output.run(jobstore)
    assert 0 == std_call
    assert "VERSION" in std_output


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
        unitName="Hello World",
    )
    job_output = ContainerizedCheckOutputJob(
        options=options,
        unitName="Hello World",
    )

    # Run jobs
    std_call = job_call.run(jobstore)
    std_output = job_output.run(jobstore)
    assert 0 == std_call
    assert workdir in std_output
{% endif %}
