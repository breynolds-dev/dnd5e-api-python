# D&D 5e API

This project started because a friend and I were trying to build a character
creator in Rails for 5th Edition. With the amount of data required we decided to
try and split the project into three parts.  The API which you will see here, a
gem wrapper library for the API that can be included on any Ruby project, and
then the character creator itself.

This is still under development so excuse the mess of code.

# Requirements

This project uses a Python virutal environment to handle dependencies, but you
will need to install `direnv` to properly handle the setting of global variables
in the environment.

Once `direnv` is installed and configured you will need to cd into the project
directory and do a `direnv allow` to allow the variables to be set anytime you
enter or exit the directory.

To install the python dependencies you need to run `pip install requirements.txt`
or `pip3 install requirements.txt` depending on which version of Python you have
installed. This project was developed using Python 3.5.