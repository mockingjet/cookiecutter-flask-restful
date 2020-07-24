import pathlib
import subprocess

from setuptools import setup, find_packages
from setuptools.command.install import install
from setuptools.command.develop import develop


__requires__ = ['pipenv']

packages = find_packages("{{cookiecutter.app_slug}}")
base_dir = pathlib.Path.cwd()

pipenv_command = ['pipenv', 'install', '--deploy', '--system']
pipenv_command_dev = ['pipenv', 'install', '--dev', '--deploy', '--system']


class PostDevelopCommand(develop):
    def run(self):
        subprocess.check_call(pipenv_command_dev)
        develop.run(self)


class PostInstallCommand(install):
    def run(self):
        subprocess.check_call(pipenv_command)
        install.run(self)


with open(base_dir / 'README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='{{cookiecutter.app_name}}',
    version="0.1.0",
    description="{{cookiecutter.app_short_description}}",
    long_description='\n' + long_description,
    author="{{cookiecutter.full_name}}",
    packages=packages,
    cmdclass={
        'develop': PostDevelopCommand,
        'install': PostInstallCommand,
    },
)
