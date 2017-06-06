# D&D 5e API

This project started because a friend and I were trying to build a character
creator in Rails for 5th Edition. With the amount of data required we decided to
try and split the project into three parts.  The API which you will see here, a
gem wrapper library for the API that can be included on any Ruby project, and
then the character creator itself.

This is still under development so excuse the mess of code.

# Requirements

This project uses a Python virtual environment to handle dependencies, but you
will need to install `direnv` to properly handle the setting of global variables
in the environment.

Once `direnv` is installed and configured you will need to cd into the project
directory and create a file called `.envrc`.  Copy and past the following lines
into this file:


```
source venv/bin/activate
export FLASK_APP="run.py"
export SECRET="YOUR_SECRET_STRING"
export APP_SETTINGS="development"
export DATABASE_URL="postgresql+psycopg2://USERNAME:PASSWORD@localhost/dnd5e_api"
```

Replace the secret string, and username and password with your information then
save the file. Once saved it might prompt you to allow this file to be executed
by direnv, you simply need to type `direnv allow`.  This means that any time you
change into this directory it will execute the lines inside of this file.  This
activates your virtual environment and sets a few of the environmental keys that
are required.

To install the python dependencies you need to run `pip install requirements.txt`
or `pip3 install requirements.txt` depending on which version of Python you have
installed. This project was developed using Python 3.5.
