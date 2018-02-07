"""{{cookiecutter.project_slug}} jobs."""

import subprocess

from toil.job import Job
import docker

from {{cookiecutter.project_slug}} import singularity


class BaseJob(Job):

    """Job base class used to share variables and methods across steps."""

    def __init__(self, options=None, lsf_tags=None, unitName="", **kwargs):
        """
        Use this base class to share variables across pipelines steps.

        Arguments:
            unitName (str): string that will be used as the lsf jobname.
            options (object): an argparse name space object.
            lsf_tags (list): a list of custom supported tags by leukgen
                see this file /ifs/work/leukgen/opt/toil_lsf/python2/lsf.py.
            kwargs (dict): key word arguments to be passed to toil.job.Job.
        """
        # If unitName is not passed, we set the class name as the default.
        if unitName == "":
            unitName = self.__class__.__name__

        # This is a custom solution for LSF options in leukgen, ask for lsf.py.
        if getattr(options, "batchSystem", None) == "LSF":
            unitName = "" if unitName is None else str(unitName)
            unitName += "".join("<LSF_%s>" % i for i in lsf_tags or [])

        # make options an attribute.
        self.options = options

        # example of a shared variable.
        self.shared_variable = "Hello World"

        super(BaseJob, self).__init__(unitName=unitName, **kwargs)

    def check_call(self, cmd, cwd=None, env=None):
        """
        Wrap the subprocess.check_call, if any container tool was chosen.

        Arguments:
            cmd (list): list of command line arguments passed to the tool.
            cwd (str): current working directory.
            env (dict): environment variables to set inside container.

        Returns:
            int: 0 if call succeed else non-0.
        """
        if self.options.singularity:
            return self.singularity_call(
                cmd,
                cwd=cwd,
                check_output=False,
                env=env
                )
        elif self.options.docker:
            return self.docker_call(
                cmd,
                cwd=cwd,
                check_output=False,
                env=env
                )
        return subprocess.check_call(
            cmd,
            cwd=cwd,
            env=env
            )

    def check_output(self, cmd, cwd=None, env=None):
        """
        Wrap the subprocess.check_output, if any container tool was chosen.

        Arguments:
            cmd (list): list of command line arguments passed to the tool.
            cwd (str): current working directory.
            env (dict): environment variables to set inside container.

        Returns:
            str: stdout of the system call.
        """
        if self.options.singularity:
            return self.singularity_call(
                cmd,
                cwd=cwd,
                check_output=True,
                env=env
                )
        elif self.options.docker:
            return self.docker_call(
                cmd,
                cwd=cwd,
                check_output=True,
                env=env
                )
        return subprocess.check_output(
            cmd,
            cwd=cwd,
            env=env
            )

    def singularity_call(self, cmd, cwd=None, env=None, check_output=False):
        """
        Call the base singularity call, sending the singularity parameters
        needed for managing the shared and working directories.

        Arguments:
            cmd (list): list of command line arguments passed to the tool.
            cwd (str): current working directory.
            env (dict): environment variables to set inside container.
            check_output (bool): check_output or check_call behavior.

        Returns:
            str: (check_output=True) stdout of the system call.
            int: (check_output=False) 0 if call succeed else non-0.
        """
        singularity_parameters = []

        # Set parameters for managing directories if options are defined
        if self.options.shared_fs:
            singularity_parameters += [
                "--bind", "{fs}:{fs}".format(fs=self.options.shared_fs)
                ]
        if self.options.workDir:
            singularity_parameters += [
                "--contain",
                "--workdir", self.options.workDir
                ]
        if cwd:
            singularity_parameters += ["--pwd", cwd]

        return singularity.singularity_call(
            self.options.singularity,
            parameters=cmd,
            singularity_parameters=singularity_parameters,
            check_output=check_output,
            environment=env
            )

    def docker_call(self, cmd, cwd=None, env=None, check_output=False):
        """
        Call the base singularity call, sending the singularity parameters
        needed for managing the shared and working directories.

        Arguments:
            cmd (list): list of command line arguments passed to the tool.
            cwd (str): current working directory.
            env (dict): environment variables to set inside container.
            check_output (bool): check_output or check_call behavior.

        Returns:
            str: (check_output=True) stdout of the system call.
            int: (check_output=False) 0 if call succeed else non-0.
        """
        docker_parameters = {}
        docker_parameters['command'] = cmd
        docker_parameters['detach'] = check_output
        docker_parameters['entrypoint'] = ''
        docker_parameters['environment'] = env or {}
        docker_parameters['volumes'] = {}

        # Set parameters for managing directories if options are defined
        if self.options.shared_fs:
            docker_parameters['volumes'][self.options.shared_fs] = {
                'bind': self.options.shared_fs,
                'mode': 'rw'
                }

        if self.options.workDir:
            docker_parameters['volumes'][self.options.workDir] = {
                'bind': '/tmp',
                'mode': 'rw'
                }

        if cwd:
            docker_parameters['working_dir'] = cwd

        # Clean created docker containers where
        client = docker.from_env()
        for container in client.containers.list(all=True):
            if container.name == self.options.docker:
                container.stop()
                container.remove()
        try:
            output = client.containers.run(
                self.options.docker,
                **docker_parameters
                )
        # If the container exits with a non-zero exit code and detach is False.
        except (
            ContainerError,
            ImageNotFound,
            subprocess.CalledProcessError
            ) as stderr:
            raise subprocess.CalledProcessError(0, cmd=cmd, output=stderr)

        return output.logs() if check_output else 0


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
