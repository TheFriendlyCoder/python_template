Overview
========

This is a template project I use for my personal projects, to remind me how
to set up projects, folder structures, etc. and how to integrate the projects
with Travis CI, PyPI, and other such services.

Creating a new project
-----------------------

* clone the project files
* update all references to 'ksp_sample' in all files to the name of the new project
  * ./docs/conf.py
  * ./setup.py
  * ./tox.ini
  * ./README.rst
  * ./.travis.yml
  * ./tests/test_version.py
* update all references to "python_template" in all files to the name of the new project
  * ./README.rst
* rename the 'src/ksp_sample' subfolder to reflect the new project name
* update the project specific parameters in the setup.py file in the root folder
* activate project on `travis-ci.org <https://travis-ci.org/>`_

  * log in to the Travis CI website
  * hover over your avatar in the top-right corner and select 'settings'
  * click the "sync account" button in the left side-bar
  * refresh your browser page to make sure your list of projects is up to date
  * find your project in the list and click the slider to turn on support
  * click the small cog icon next to your new project to configure settings
  * Under environment variables, define the following variables (needed to publish Python packages):

    * *DEPLOY_USER* User name to log in to PyPI package repository
    * *DEPLOY_PASS* Password for the PyPI user

  * Under cron set the master branch to build once a month
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
