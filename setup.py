#!/usr/bin/env python
"""Setuptools packaging script for the project"""
import os
import ast
from setuptools import setup, find_packages

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# project specific parameters
PROJECT_NAME = 'ksp_sample'
PROJECT_DEPENDENCIES = [
    'six'
]
PROJECT_DEV_DEPENDENCIES = [
    'twine',
    'pytest',
    'pytest-cov',
    'mock',
    'pylint',
    'sphinx',
    'tox']
PROJECT_DESCRIPTION = 'Project Short Description'
PROJECT_KEYWORDS = 'space separated tags'
PROJECT_SUPPORTED_PYTHON_VERSION = \
    ">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, <4"
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=


def load_console_scripts(project):
    """Generates list of 'entry point' functions for use by Python setup tools

    Each element in this list defines the name and entry point function for each
    python script included with the current project that is to be exposed to
    user's shells when the package is installed.

    This script assumes that any python script found in a folder named 'scripts'
    under the project folder is to be exposed on the shell during deployment.
    Further, this script assumes that all such scripts expose a public function
    called 'main' which will act as the primary entry point for the script. This
    function will then be responsible for parsing any supported command line
    parameters and executing the appropriate functionality.

    The output from this function can be provided to the setuptools.setup()
    function, something like this:

    entry_points={
        'console_scripts': load_console_scripts(project_name)
    }

    :param str project:
        the name of the current project. It is also assumed that the project
        sources will be located under a sub-folder of the same name.
    :return:
        list of shell scripts exposed by this project. Produces an empty
        list if there are no shell scripts supported by the project.
    """
    scripts_path = os.path.join(project, 'scripts')
    if not os.path.exists(scripts_path):
        return []

    scripts_namespace = "{0}.scripts".format(project)
    retval = []

    py_scripts = os.listdir(scripts_path)
    for py_file in py_scripts:
        file_parts = os.path.splitext(py_file)
        if file_parts[1] == ".py" and file_parts[0] != '__init__':
            script_config = "{0}={1}.{0}:main".format(
                file_parts[0],
                scripts_namespace
            )
            retval.append(script_config)

    return retval


def _verify_src_version(version):
    """Checks to make sure an arbitrary character string is a valid version id

    Version numbers are expected to be of the form X.Y.Z

    :param str version: string to validate
    :returns: True if the string is a version number, else false
    :rtype: :class:`bool`
    """
    if not isinstance(version, str):
        return False
    if "." not in version:
        return False
    parts = version.split(".")
    if len(parts) != 3:
        return False

    for cur_part in parts:
        if not cur_part.isdigit():
            return False
    return True


def _src_version(project):
    """Parses the version number from the source project

    :param str project: the name of the project to get the version for
    :returns: the version for the specified project
    :rtype: :class:`str`
    """
    # To prevent circular dependencies between the setup script and the
    # project code, we need to parse the version.py file independently
    # without importing anything from the project itself
    retval = None

    ver_path = os.path.join(os.getcwd(), 'src', project, 'version.py')
    assert os.path.exists(ver_path)

    with open(ver_path) as ver_file:
        data = ver_file.read()

    for cur_node in ast.parse(data).body:
        # We only care about assignment statements, as we look for a line
        # that resembles `__version__ = "1.2.3"`
        if not isinstance(cur_node, ast.Assign):
            continue

        # In the off chance that there are multiple assignment statements
        # in our version file, lets search for one that involves a variable
        # named "__version__"
        found_version = False
        for cur_target in cur_node.targets:
            if cur_target.id == "__version__":
                found_version = True
                break
        if not found_version:
            continue

        assert isinstance(cur_node.value, ast.Str)

        retval = cur_node.value.s
        break

    assert retval is not None
    assert _verify_src_version(retval)
    return retval


def get_version_number(project):
    """Retrieves the version number for a project"""

    retval = _src_version(project)

    if 'TRAVIS_TAG' in os.environ and not os.environ['TRAVIS_TAG'] == '':
        # HACK: Let us assume we're going to use the tag name
        #       when building the template project. Makes it
        #       easier to test release builds
        if project == "ksp_sample":
            return os.environ['TRAVIS_TAG']

        # make sure the tag name matches our version number
        if not os.environ['TRAVIS_TAG'] == retval:
            raise Exception("Tag {0} is expected to be {1}".format(
                os.environ['TRAVIS_TAG'],
                retval
            ))
        # If we build from a tag, just use the version number verbatim
        return retval

    # Pre release versions need a non-numeric suffix on the version number
    retval += ".dev"
    if 'TRAVIS_BUILD_NUMBER' in os.environ:
        retval += os.environ['TRAVIS_BUILD_NUMBER']
    else:
        retval += "0"

    return retval


def generate_readme(project):
    """Generates a readme for the Python package, based on the readme file

    :param str project: name of the project to generate the readme for
    :returns: readme text for the package
    :rtype: :class:`str`
    """
    print(project)
    headers = list()
    headers.append({
        "image": "https://travis-ci.org/TheFriendlyCoder/python_template.svg?branch=master",
        "target": "https://travis-ci.org/TheFriendlyCoder/python_template",
        "text": "Build Automation"
    })
    headers.append({
        "image": "https://coveralls.io/repos/github/TheFriendlyCoder/python_template/badge.svg?branch=master",
        "target": "https://coveralls.io/github/TheFriendlyCoder/python_template?branch=master",
        "text": "Test Coverage"
    })
    headers.append({
        "image": "https://img.shields.io/pypi/pyversions/ksp_sample.svg",
        "target": "https://pypi.python.org/pypi/ksp_sample",
        "text": "Python Versions"
    })
    headers.append({
        "image": "https://readthedocs.org/projects/ksp_sample/badge/?version=latest",
        "target": "http://ksp_sample.readthedocs.io/en/latest/?badge=latest",
        "text": "Documentation Status"
    })
    headers.append({
        "image": "https://requires.io/github/TheFriendlyCoder/python_template/requirements.svg?branch=master",
        "target": "https://requires.io/github/TheFriendlyCoder/python_template/requirements/?branch=master",
        "text": "Requirements Status"
    })
    headers.append({
        "image": "https://img.shields.io/pypi/format/ksp_sample.svg",
        "target": "https://pypi.python.org/pypi/ksp_sample/",
        "text": "Package Format"
    })
    headers.append({
        "image": "https://img.shields.io/pypi/dm/ksp_sample.svg",
        "target": "https://pypi.python.org/pypi/ksp_sample/",
        "text": "Download Count"
    })
    headers.append({
        "image": "https://img.shields.io/pypi/l/ksp_sample.svg",
        "target": "https://www.gnu.org/licenses/gpl-3.0-standalone.html",
        "text": "GPL License"
    })

    header_template = """.. image:: {0}
    :target: {1}
    :alt: {2}

    """

    retval = ""
    for cur_header in headers:
        retval += header_template.format(cur_header["image"], cur_header["target"], cur_header["text"])
        retval += "\n"

    retval += open('README.rst').read()

    return retval

# Execute packaging logic
setup(
    name=PROJECT_NAME,
    version=get_version_number(PROJECT_NAME),
    author='Kevin S. Phillips',
    author_email='thefriendlycoder@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    description=PROJECT_DESCRIPTION,
    long_description=generate_readme(PROJECT_NAME),
    url='https://github.com/TheFriendlyCoder/' + PROJECT_NAME,
    keywords=PROJECT_KEYWORDS,
    entry_points={
        'console_scripts': load_console_scripts(PROJECT_NAME)
    },
    install_requires=PROJECT_DEPENDENCIES,
    python_requires=PROJECT_SUPPORTED_PYTHON_VERSION,
    extras_require={
        'dev': PROJECT_DEV_DEPENDENCIES
    },
    license="GPL",
    # https://pypi.org/classifiers/
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "License :: OSI Approved :: "
        "GNU General Public License v3 or later (GPLv3+)",
        "Topic :: Software Development :: Libraries",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
    ]
)
