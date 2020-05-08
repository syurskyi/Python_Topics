[![Build Status](https://travis-ci.org/martialblog/python-unittest-presentation.svg?branch=master)](https://travis-ci.org/martialblog/python-unittest-presentation)

# python-unittest-presentation
Presentation and examples of Unit Testing in Python.

# Usage

## Git

```bash
$ git clone https://github.com/martialblog/python-unittest-presentation.git
```

## Sieve of Eratosthenes

Simple mathematical function with various ways of testing.

```bash
$ cd code/sieve

$ # Manual Tests
$ python3 main.py (1|2|3)

$ # Unit Tests
$ python3 -m unittest sieve_test.py
```

## Simple Tagger

A simple POS-Tagger with tests in py.test and Unittest.

```bash
$ cd code/nlp

$ pip3 install -r requirements.txt

$ # Unittest
$ python3 -m unittest tests/unittest_nlp.py

$ # nose2
$ nosetests tests/unittest_nlp.py

$ # py.test
$ py.test tests/pytest_nlp.py
$ py.test tests/unittest_nlp.py
```

## Exercise

You will find some classes and functions in *exercise.py* and some Unittest boilerplate.

```bash
$ cd code/exercise

$ # Run Unit Tests
$ python3 -m unittest discover
```

Some assert functions:

```python
assertEqual(a, b)
assertNotEqual(a, b)
assertAlmostEqual(a, b)
assertTrue(x)
assertIs(a, b)
assertIsNone(x)
```
