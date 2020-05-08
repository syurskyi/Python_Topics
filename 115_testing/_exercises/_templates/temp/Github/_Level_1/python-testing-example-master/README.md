# python-testing-example
Example of Unittesting, Code Coverage and Code Style Checks being baked in

https://github.com/lathama/python-testing-example

Enabling your software to run its tests on every execution can be helpful
to all parties. This can remove complexity with CI and local development stacks

This is an example only meant to demonstrate the idea.

* If run with the Python debugging option tests, coverage and style will 
  attempted.

* If Python Coverage is installed or the source is in "libraries" directory 
  then code coverage will be run

* If pycodestyle is installed or the source is in "libraries" directory
  then style checks will be run

* Unit Testing will not exit on error but will log to unittesting.log

* Actions driven by the module's `__init__.py` so look there.

