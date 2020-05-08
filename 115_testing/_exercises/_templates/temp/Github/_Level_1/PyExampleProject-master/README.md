# VSCode Sample Project

## Extensions

|Name|Notes|
|---|---|---|
|[Python](https://marketplace.visualstudio.com/items?itemName=donjayamanne.python)|Intellisense, debugging, linting, etc
|[EditorConfig](https://marketplace.visualstudio.com/items?itemName=EditorConfig.EditorConfig)|Makes .editorconfig files work to make sure we keep our editors from doing stupid things.

## virtualenv

This project assumes you have a virtualenv directory of `venv` located in the root of this directory. 

## Python Version

We set the python version in `.vscode/settings.json`
```
"python.pythonPath": "${workspaceRoot}/venv/bin/python"
```
which will pull the python version from the virtualenv directory. This allows it to work with whatever python version you use to create your virtualenv. 

To use with python3 you can use do the following:
```
python3 -m pip install virtualenv
python3 -m virtualenv venv
source venv/bin/activate
``` 

## PyLint

In order to have PyLint work flexibly with whatever version of python you are using we also set the PyLint directory in the `.vscode/settings.json` file:

```
"python.linting.pylintPath": "${workspaceRoot}/venv/bin/pylint"
```
To make this work, once you have your virtualenv created you need to run:
```
source venv/bin/activate # if not already in it
pip install pylint
```

## Debugging
Some various debugging modes are configured in `.vscode/launch.json` but may need to be further configured to actually work (Remote Debugging for example).
The different configurations in `.vscode/launch.json` control what options are available to you in the debug dropdown next to the play button. 

For more information on configuring these see [here](https://github.com/DonJayamanne/pythonVSCode/wiki/Debugging). 

## Coverage
In order to check test coverage we can use `coverage.py` with the command:
```
coverage erase # Erase previous coverage run data
coverage run -m unittest 
coverage report
```
