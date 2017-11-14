"""{{cookiecutter.project_slug}} pipeline."""

import subprocess

from toil.common import Toil
from toil.job import Job

from {{cookiecutter.project_slug}} import __version__
from {{cookiecutter.project_slug}} import exceptions


class BaseJob(Job):

    """Job base class used to share variables and methods across steps."""

    def __init__(
            self, options=None, lsf_tags=list(), unitName="", *args, **kwargs
            ):
        """
        Use this base class to share variables across pipelines steps.

        Arguments:
            unitName (str): string that will be used as the lsf jobname.
            options (object): an argparse name space object.
            lsf_tags (list): a list of custom supported tags by leukgen
                see this file /ifs/work/leukgen/opt/toil_lsf/python2/lsf.py.
        """
        # Load tags.
        if options.batchSystem == "LSF":
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
        subprocess.check_call(["echo", self.shared_variable])


class HelloWorldMessage(BaseJob):

    def __init__(self, message, *args, **kwargs):
        """Load message variable as attribute."""
        self.message = message
        super(HelloWorldMessage, self).__init__(*args, **kwargs)

    def run(self, fileStore):
        """Send message to the world."""
        subprocess.check_call(["echo", self.message])


def run_pipeline():
    """Toil implementation for {{cookiecutter.project_slug}}."""
    options = get_options()

    helloworld = HelloWorld(
        cores=4,
        memory="12G",
        options=options,
        unitName=options.jobname + " Hello World",
        lsf_tags=["SHORT"]
        )

    helloworld_message = HelloWorldMessage(
        message="Hello Universe",
        cores=4,
        memory="12G",
        options=options,
        unitName=options.jobname + " Hello World with Message",
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


def get_options():
    """Get pipeline configuration using toil's argparse."""
    parser = Job.Runner.getDefaultArgumentParser()

    # Add description to parser.
    parser.description = "Run {{cookiecutter.project_slug}} pipeline."

    # We need to add a group of arguments specific to the pipeline.
    settings = parser.add_argument_group("Pipeline Configuration")

    settings.add_argument(
        "-v", "--version",
        action="version",
        version="%(prog)s " + __version__
        )

    settings.add_argument(
        "--jobname",
        help="Base name to be passed to jobs.",
        required=True
        )

    options = parser.parse_args()

    # Make sure the toil logs directory exists.
    if options.writeLogs is not None:
        subprocess.check_call(["mkdir", "-p", options.writeLogs])

    return options
