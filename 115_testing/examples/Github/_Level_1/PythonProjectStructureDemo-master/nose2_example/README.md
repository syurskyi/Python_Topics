# Python nose2 unittesting example
This is an example package setup for having unittests in a separate folder from the actual package.

Run the unittests from this top folder (where this README is) with:
```bash
nose2
``` 

You don't need to modify the PYTHONPATH or install the package (optionally with virtualenv) to make this work. By default python uses the current path to look for a package first. By running `nose2` from the this directory, python finds the package just fine.

The package contains both absolute and relative import to show how they work. In subpackage/utils.py I actually import from the parent directory with an absolute import. This will work both with nose2 for unittesting, but also when the package is installed in the global or virtualenv pythonpath.

This is an example output:
```bash
[dolf@arch unittesting_example]$ nose2
....
----------------------------------------------------------------------
Ran 4 tests in 0.001s

OK
```
