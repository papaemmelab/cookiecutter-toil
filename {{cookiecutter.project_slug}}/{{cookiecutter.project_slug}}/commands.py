"""{{cookiecutter.project_slug}} pipeline."""
{% if cookiecutter.cli_type == "toil" %}
import argparse
import subprocess

from toil.common import Toil
from toil.job import Job
import click

from {{cookiecutter.project_slug}} import __version__


class BaseJob(Job):

    """Job base class used to share variables and methods across steps."""

    def __init__(
            self, options=None, lsf_tags=None, unitName="", *args, **kwargs):
        """
        Use this base class to share variables across pipelines steps.

        Arguments:
            unitName (str): string that will be used as the lsf jobname.
            options (object): an argparse name space object.
            lsf_tags (list): a list of custom supported tags by leukgen
                see this file /ifs/work/leukgen/opt/toil_lsf/python2/lsf.py.
            args (list): arguments to be passed to toil.job.Job.
            kwargs (dict): key word arguments to be passed to toil.job.Job.
        """
        # If unitName is not passed, we set the class name as the default.
        if unitName == "":
            unitName = self.__class__.__name__

        # This is a custom solution for LSF options in leukgen, ask for lsf.py.
        if options.batchSystem == "LSF":
            lsf_tags = lsf_tags or list()
            unitName = "" if unitName is None else str(unitName)
            unitName += "".join("<LSF_%s>" % i for i in lsf_tags)

        # make options an attribute.
        self.options = options

        # example of a shared variable.
        self.shared_variable = "Hello World"

        super(BaseJob, self).__init__(unitName=unitName, *args, **kwargs)


class HelloWorld(BaseJob):

    def run(self, fileStore):
        """Say hello to the world."""
        with open(self.options.outfile, "w") as outfile:
            outfile.write(self.shared_variable)


class HelloWorldMessage(BaseJob):

    def __init__(self, message, *args, **kwargs):
        """Load message variable as attribute."""
        self.message = message
        super(HelloWorldMessage, self).__init__(*args, **kwargs)

    def run(self, fileStore):
        """Send message to the world."""
        with open(self.options.outfile, "w") as outfile:
            outfile.write(self.options.message)

        # Log message to master.
        fileStore.logToMaster(self.message)


def run_toil(options):
    """Toil implementation for {{cookiecutter.project_slug}}."""
    helloworld = HelloWorld(
        cores=4,
        memory="12G",
        options=options,
        unitName="Hello World",
        lsf_tags=["SHORT"]
        )

    helloworld_message = HelloWorldMessage(
        message=options.message,
        cores=4,
        memory="12G",
        options=options,
        unitName="Hello World with Message",
        lsf_tags=["INTERNET"]
        )

    # Build pipeline DAG.
    helloworld.addChild(helloworld_message)

    # Execute the pipeline.
    with Toil(options) as pipe:
        if not pipe.options.restart:
            pipe.start(helloworld)
        else:
            pipe.restart()


def get_parser():
    """Get pipeline configuration using toil's argparse."""
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
        )

    # Add Toil options.
    Job.Runner.addToilOptions(parser)

    # Add description to parser.
    parser.description = "Run {{cookiecutter.project_slug}} pipeline."

    # We need to add a group of arguments specific to the pipeline.
    settings = parser.add_argument_group("{{cookiecutter.project_slug}} configuration")

    settings.add_argument(
        "-v", "--version",
        action="version",
        version="%(prog)s " + __version__
        )

    settings.add_argument(
        "--message",
        help="A message to be echoed to the Universe.",
        required=False,
        default="Hello Universe, this text is used in the pipeline tests.",
        )

    settings.add_argument(
        "--total",
        help="Total times message should be printed.",
        required=False,
        default=1,
        type=int,
        )

    settings.add_argument(
        "--outfile",
        help="Outfile to print message to.",
        required=True,
        type=click.Path(file_okay=True, writable=True),
        )

    return parser


def validate_options(options):
    """Perform validations and add post parsing attributes to `options`."""
    if options.writeLogs is not None:
        subprocess.check_call(["mkdir", "-p", options.writeLogs])

    # This is just an example of
    options.message = options.message * options.total

    return options


def main():
    """Parse options and run toil."""
    options = get_parser().parse_args()
    options = validate_options(options=options)
    run_toil(options=options)

if __name__ == "__main__":
    main()
{% elif cookiecutter.cli_type == "click" %}
import click


@click.command()
@click.option("--message", default="Hello World")
def hello_world(message):
    """Echo message and exit."""
    click.echo(message)
{% endif %}