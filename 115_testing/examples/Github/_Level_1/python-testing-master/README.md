# Python unittesting examples

This project has some examples on how to write simple unittest in python.

It covers the basic topics like:
- setUp and tearDown 
- assertion
- skipping tests
- using mocks
- example for testing with and without a framework (see id_creator)

## Running the tests

It is possible to run all tests in the project or be more specific and even run one single testcase.
Below are some examples on the different ways of running the tests:

- `python3 -m unittest`
- `python3 -m unittest test_assertions`
- `python3 -m unittest test_assertions.TestAssertions`
- `python3 -m unittest test_assertions.TestAssertions.test_equality`

It is also possible to use the build in function from unittest and run the tests by creating following function:
```
if __name__ == '__main__':
    unittest.main()
```

See _**test_setup_teardown.py**_

## Useful links to learn more about testing in python

- [Python 3 unittest docs](https://docs.python.org/3/library/unittest.html)
- [Python 3 unittest mock docs](https://docs.python.org/3/library/unittest.mock.html)
