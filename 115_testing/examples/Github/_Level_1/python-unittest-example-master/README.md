# Example Python Unit Test Project

The test rig in tests/ should provide a unit test with 100% code
coverage of the Distance class in src/ .


# Running

From the parent directory, you should be able to run the test with
the following command:

```
$ python3 -m tests.test_distance
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```


# Code Coverage

If you have coverage.py installed, you can use it to check the
code coverage of the test:


```
$ coverage3 run -m tests.test_distance
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
$ coverage3 report
Name                     Stmts   Miss  Cover
--------------------------------------------
src/__init__.py              0      0   100%
src/distance.py             16      0   100%
tests/__init__.py            0      0   100%
tests/test_distance.py      16      0   100%
--------------------------------------------
TOTAL                       32      0   100%
```
