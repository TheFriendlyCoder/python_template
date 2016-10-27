Overview
========
.. image:: https://travis-ci.org/TheFriendlyCoder/proj_name.svg?branch=master
    :target: https://travis-ci.org/TheFriendlyCoder/proj_name
    :alt: Build Automation

.. image:: https://coveralls.io/repos/github/TheFriendlyCoder/proj_name/badge.svg?branch=master
    :target: https://coveralls.io/github/TheFriendlyCoder/proj_name?branch=master
    :alt: Test Coverage

.. image:: https://img.shields.io/pypi/pyversions/proj_name.svg
    :target: https://pypi.python.org/pypi/proj_name
    :alt: Python Versions

.. image:: https://readthedocs.org/projects/proj_name/badge/?version=latest
    :target: http://proj_name.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. image:: https://requires.io/github/TheFriendlyCoder/proj_name/requirements.svg?branch=master
     :target: https://requires.io/github/TheFriendlyCoder/proj_name/requirements/?branch=master
     :alt: Requirements Status

.. image:: https://img.shields.io/pypi/format/proj_name.svg
    :target: https://pypi.python.org/pypi/proj_name/
    :alt: Package Format

.. image:: https://img.shields.io/pypi/dm/proj_name.svg
    :target: https://pypi.python.org/pypi/proj_name/
    :alt: Download Count

.. image:: https://img.shields.io/pypi/l/proj_name.svg
    :target: https://www.gnu.org/licenses/gpl-3.0-standalone.html
    :alt: GPL License

Project Short Description

Creating a new project:
 * clone the project files
 * update all references to 'proj_name' in all files to the name of the new project
 * rename the 'proj_name' subfolder to reflect the new project name
 * update the project specific parameters in the setup.py file in the root folder
 * log in to travis-ci.org and activate the new project
 * log in to readthedocs.org and activate the new project
 * log in to coveralls.io and activate the new project
 * log in to requires.io and activate the new project
 * modify the 'fail_under' value in the .coveragerc file to a reasonable value for unit test coverage (ie: 90% say)
 * For consistency, set the following to the same 'short descriptive' text for the project:
    * title on GitHub project
    * description of readthedocs page
    * DistUtils project short description in the setup.py
    * first line of the readme.rst

Using the project;
 * to generate a package do the following: python setup.py bdist_wheel
 * to upload a new version to pypi, do the following: twine upload ./dist/*.whl
 * update API docs as follows: sphinx-apidoc --force --separate -o ./docs proj_name
 * to generate HTML docs run the following from the root folder: python setup.py build_sphinx
 * make sure to add any new project dependencies to the setup.py as requirements change
 * make sure to separate out development dependencies from runtime dependencies

TIPS:
 * make sure your project name doeesn't use underscores because pypi packages will convert them to dashes
 * to make some of the badges work you'll need to upload a version to pypi
 * you need to generate a package first before using twine to upload it to pypi
 * all development work should be done in a local virtual environment under a ./venv subfolder (ie: virtualenv -p
 python3 ./venv && . ./venv/bin/activate)
 * you can add PyCharm projects to the repo. Just exclude the files listed in the .gitignore file.

Links:
 * badge related blog: http://thomas-cokelaer.info/blog/2014/08/1013/
