"""{{cookiecutter.project_slug}} pasers."""

import argparse

from toil.common import Toil
from toil.job import Job
import click

from {{cookiecutter.project_slug}} import __version__
from {{cookiecutter.project_slug}} import utils


class _ToilHelpAction(argparse._HelpAction):

    def __call__(self, parser, namespace, values, option_string=None):
        """Print parser help and exist whilst adding a flag to the parser."""
        parser.show_toil_groups = True
        parser.print_help()
        parser.exit()


class ToilArgumentParser(argparse.ArgumentParser):

    """
    A Argument parser for toil pipelines.

    Toil options are automatically added, but hidden by default in the
    help print. However, the custom `--help-toil` option will include
    toil arguments sections in the help print.

    Additionally, a container section is included (this can be turned off).
    """

    def __init__(self, add_container_group=True, add_version=True, **kwargs):
        """
        Add Toil options, `--help-toil` and container section to parser.

        Arguments:
            add_container_group (bool): add section for container runs.
            add_version (bool): add version option using `__version__`.
            kwargs (dict): keyword dict for `argparse.ArgumentParser`.
        """
        if not kwargs.get("formatter_class", None):
            kwargs["formatter_class"] = argparse.ArgumentDefaultsHelpFormatter

        super(ToilArgumentParser, self).__init__(**kwargs)

        # Add toil options.
        Job.Runner.addToilOptions(self)

        self.add_argument(
            "--help-toil",
            action=_ToilHelpAction, default=argparse.SUPPRESS,
            help="print help with Toil options and exit"
        )

        # Add package version.
        if add_version:
            self.add_argument(
                "-v", "--version",
                action="version",
                version="%(prog)s " + __version__
            )

        # Parameters to run with docker or singularity.
        self.add_container_group = add_container_group
        if add_container_group:
            settings = self.add_argument_group(
                "Run with docker or singularity:"
                )

            settings.add_argument(
                "--docker",
                help="Name of the docker image, available in daemon.",
                default=False,
                metavar="DOCKER-IMAGE-NAME",
            )

            settings.add_argument(
                "--singularity",
                help=(
                    "Path of the singularity image (.simg) to jobs be run "
                    "inside singularity containers."
                ),
                required=False,
                metavar="SINGULARITY-IMAGE-PATH",
                type=click.Path(
                    file_okay=True,
                    readable=True,
                    resolve_path=True,
                    exists=True,
                )
            )

            settings.add_argument(
                "--shared-fs",
                help="Shared file system directory to be mounted in containers",
                required=False,
                type=click.Path(
                    file_okay=True,
                    readable=True,
                    resolve_path=True,
                    exists=True,
                )
            )

    def format_help(self):
        """Include toil options if `self.show_toil_groups` is True."""
        formatter = self._get_formatter()

        # usage
        formatter.add_usage(
            self.usage,
            self._actions,
            self._mutually_exclusive_groups
        )

        # description
        formatter.add_text(self.description)

        # positionals, optionals and user-defined groups
        for action_group in self._action_groups:

            # Decide whether to show toil options or not.
            show_toil_groups = getattr(self, "show_toil_groups", False)
            is_toil_group = action_group.title.startswith('toil')
            is_toil_group |= 'Logging Options' in action_group.title

            if not is_toil_group or (is_toil_group and show_toil_groups):
                formatter.start_section(action_group.title)
                formatter.add_text(action_group.description)
                formatter.add_arguments(action_group._group_actions)
                formatter.end_section()

        # epilog
        formatter.add_text(self.epilog)

        # determine help from format above
        return formatter.format_help()

    def parse_args(self, *args, **kwargs):
        """Validate parsed options."""
        args = super(ToilArgumentParser, self).parse_args(*args, **kwargs)

        # Check container options are ok.
        if self.add_container_group:
            if args.singularity and args.docker:
                raise click.UsageError(
                    "You can't pass both --singularity and --docker."
                )

            if args.shared_fs and not any([args.docker, args.singularity]):
                raise click.UsageError(
                    "--shared-fs should be used only with "
                    "--singularity or --docker."
                )

            if args.shared_fs and args.workDir:
                if args.shared_fs not in args.workDir:
                    raise click.UsageError(
                        "The --workDir must be available in the "
                        "--shared-fs directory."
                    )

            if args.docker and not utils.is_docker_available():
                raise click.UsageError(
                    "Docker is not currently available in your environment."
                )

            if args.singularity and not utils.is_singularity_available():
                raise click.UsageError(
                    "Singularity is not currently available in "
                    "your environment."
                )

        return args
