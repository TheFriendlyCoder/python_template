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
 * activate project on `travis-ci.org <https://travis-ci.org/>`_
   * log in to the Travis CI website
   * hover over your avatar in the top-right corner and select 'profile'
   * find your project in the list and click the slider to turn on support
   * so long as your project has a .travisci.yml file in the root folder the build should automatically start
 * activate project on `readthedocs.org <https://readthedocs.org/>`_
   * log in to the ReadTheDocs website
   * click the drop-down list on your name in the top-left corner and select "My Projects"
   * click "Import a Project"
   * To import automatically, try clicking the "Refresh" button to load your Github projects, and select the one(s) to load
   * To import manually, click "Import Manually"
   * Under "Name of Project" enter the name of the Github project without the URL or .git extension
   * Under the "Repository URL" field, copy-paste the HTTPS URL used for cloning the Github project
   * Check the "Advanced Options" check box and click "Next"
   * Fill out the advanced properties as desired
   * TBD: Travis / Github integration
 * log in to coveralls.io and activate the new project
 * log in to requires.io and activate the new project
 * modify the 'fail_under' value in the .coveragerc file to a reasonable value for unit test coverage (ie: 90% say)
 * For consistency, set the following to the same 'short descriptive' text for the project:
    * title on GitHub project
    * description of readthedocs page
    * DistUtils project short description in the setup.py
    * first line of the readme.rst

Using the project;
 * to generate a package do the following: :code:`python setup.py bdist_wheel`
 * to upload a new version to pypi, do the following: :code:`twine upload ./dist/*.whl`
 * update API docs as follows: :code:`sphinx-apidoc --force --separate -o ./docs proj_name`
 * to generate HTML docs run the following from the root folder: :code:`python setup.py build_sphinx`
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
