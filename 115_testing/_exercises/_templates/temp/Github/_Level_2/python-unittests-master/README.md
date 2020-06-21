# python-unittests
Supersimple examples how to write unit tests in Python


# Pre-requisites 
1. pipenv (package manager recommended by Python Packaging Authority) installed 
```bash
$ pip3 install --user pipenv
```

2. virtual environment activated
```bash
$ pipenv shell
```

3. packages installed 
```bash
$ pipenv install -d
```

# How to run the tests
```bash
$ python3 -m unittest
```

# Coverage
Run tests with coverage

```bash
$ coverage run -m unittest
```

Display coverage
```bash
$ coverage report
```

or export to HTML (contains lines annotated by colors) 
```bash
$ coverage html
```