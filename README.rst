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

Creating a new project
-----------------------

* clone the project files
* update all references to 'proj_name' in all files to the name of the new project
* rename the 'src/proj_name' subfolder to reflect the new project name
* update the project specific parameters in the setup.py file in the root folder
* activate project on `travis-ci.org <https://travis-ci.org/>`_

  * log in to the Travis CI website
  * hover over your avatar in the top-right corner and select 'profile'
  * find your project in the list and click the slider to turn on support
  * click the small cog icon next to your new project to configure settings
  * Enable the "Only build if a .travisci-.yml file is present" setting
  * Under environment variables, define the following variables (needed to publish Python packages):

    * *DEPLOY_USER* User name to log in to PyPI package repository
    * *DEPLOY_PASS* Password for the PyPI user

  * Under cron set the master branch to build once a month, so long as no build has run within 24 hours
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

* activate project on `coveralls.io <https://coveralls.io/>`_

  * log in to the coveralls dashboard
  * click "add repo"
  * search for new repo in the list
  * click the "on" button to enable coverage analysis

* activate project on `requires.io <https://requires.io>`_

  * log in to the requires dashboard
  * click on the "repositories" button at the top
  * wait for the project list to refresh and show your new project
  * click the "Activate" button next to your repo
  * TBD: See if I need to set up a webhook to get this working

* modify the 'fail_under' value in the .coveragerc file to a reasonable value for unit test coverage (ie: 90% say)
* For consistency, set the following to the same 'short descriptive' text for the project:

  * title on GitHub project
  * description of readthedocs page
  * DistUtils project short description in the setup.py
  * first line of the readme.rst

Using the project
-----------------

* to generate a package do the following: :code:`python setup.py bdist_wheel`
* to upload a new version to pypi, do the following: :code:`twine upload ./dist/*.whl`
* update API docs as follows: :code:`sphinx-apidoc --force --separate -o ./docs proj_name`
* to generate HTML docs run the following from the root folder: :code:`python setup.py build_sphinx`
* make sure to add any new project dependencies to the setup.py as requirements change

TIPS
----

* make sure your project name doesn't use underscores in the name because pypi packages will convert them to dashes when being published which creates a subtle discrepancy between the module name and the package name, which can lead to confusion
* make sure your project name doesn't use dashes in the name because you'll need to name your module with the dash for consistency but then the project will fail the PEP8 validation check because the name doesn't satisfy the snake-case naming requirements.
* to make some of the badges work you'll need to upload a version to pypi
* you need to generate a package first before using twine to upload it to pypi
* all development work should be done in a local virtual environment under a ./venv subfolder (ie: :code:`virtualenv -p python3 ./venv && . ./venv/bin/activate` )
* you can add PyCharm projects to the repo. Just exclude the files listed in the .gitignore file.

Links
-----

* badge related blog: http://thomas-cokelaer.info/blog/2014/08/1013/
