# %%
'''
### Project 3 - Single Inheritance - Approach
'''

# %%
'''
I'm going to use an actual Python project with folders, modules, etc for this solution.
'''

# %%
'''
This notebook is simply detailing the sequence of steps I took to get at my final solution.
'''

# %%
'''
You can download the full solution from the resources in this video, or (preferrably) directly from the
[github repo](https://github.com/fbaptiste/python-deepdive)
'''

# %%
'''
#### Virtual Environment and pytest
'''

# %%
'''
I'm going to use `pytest` for testing in this project, so you should install it into your virtual environment.
'''

# %%
'''
Note that if you are not already using virtual environments for your projects I strongly suggest you do so.
'''

# %%
'''
Creating a virtual environment is incredibly easy.

1. create a folder for your project
2. create a virtual environment named `env` (or any name you prefer) by typing this in a console from inside 
your new folder:
  - `python -m venv env`
  - note: if you have both Python 2.x and 3.x installed, you'll probably need to specify it as `python3 -m venv env`
  - you should now have a new folder called `env` inside your project folder.
3. Next you should activate your virtual environment. How you do this will differ on Windows vs Mac/Linux:
  - Windows: `env\Scripts\activate`
  - Linux/Mac: `source env/bin/activate`
  - Your command prompt shoudl now reflect the activation of the virtual environment something like `(env)` 
  at the beginning of the prompt.
'''

# %%
'''
To deactivate a virtual environment, simply type `deactivate`.
'''

# %%
'''
Next we need to install the `pytest` library. We want to install `pytest` in our virtual environment, so do this after 
**activating** your virtual environment - make sure your prompt reflects that first.

Then install `pytest` by typing this:
`pip install -U pytest`
'''

# %%
'''
That's it, you now have a virtual environment that has `pytest`.
'''

# %%
'''
#### Project Steps
'''

# %%
'''
I'm going to provide proper docstrings for every module, class, function, etc. I will use the Google style of 
docstrings, which is documented [here](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings)
'''

# %%
'''
1. Create this folder hierarchy in the project root:

```
<project root>
....app
........models
........utils
....tests
........unit
```

Note: there is no need to create packages (no `__init.py__`), we will simply use implicit namespace packages.
'''

# %%
'''
2. Create a new module (`validators.py`) inside the `app/utils` package. In that module create a helper function 
`validate_integer` that will allow us to validate that a value is an integer, optionally between a min and max 
(inclusive), and raises a `TypeError`, `ValueError` with a custom error message that can be overriden when bound 
checks fail.
'''

# %%
'''
3. Inside the `tests/unit` folder, create a new module called `test_validators.py` and create the unit tests for 
the `validate_integer` function.
'''

# %%
'''
4. Run the unit tests and make sure all the tests pass.
    - to run the unit tests, you can use your IDE's built-in way of doing it, or you can just use the command line, 
    from the root of your project: 
    
    `python -m pytest tests` 
    
    (this will run all the tests found in that folder - you can specify more specific path to limit your tests further)
'''

# %%
'''
5. In the `models` folder, create a new module file called `inventory.py`.
'''

# %%
'''
6. Implement the `Resource` class
'''

# %%
'''
7. Create a new file `test_resource.py` in the `tests` folder
'''

# %%
'''
8. Create unit tests for the `Resource` class and make sure they all pass
'''

# %%
'''
9. Create `CPU` class
'''

# %%
'''
10. Unit test `CPU` class
'''

# %%
'''
11. Create `Storage` Class
'''

# %%
'''
12. Unit test `Storage` class
'''

# %%
'''
13. Create `HDD` class
'''

# %%
'''
14. Unit test `HDD` class
'''

# %%
'''
15. Create `SDD` class
'''

# %%
'''
16. Unit test `SDD` class
'''

# %%
