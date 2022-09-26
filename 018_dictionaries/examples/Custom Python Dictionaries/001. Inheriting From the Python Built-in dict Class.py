class UpperCaseDict(dict):
    def __setitem__(self, key, value):
        key = key.upper()
        super().__setitem__(key, value)


numbers = UpperCaseDict()
numbers["one"] = 1
numbers["two"] = 2
numbers["three"] = 3

numbers
# {'ONE': 1, 'TWO': 2, 'THREE': 3}

numbers = UpperCaseDict({"one": 1, "two": 2, "three": 3})
numbers
# {'one': 1, 'two': 2, 'three': 3}

numbers = UpperCaseDict()
numbers["one"] = 1
numbers["two"] = 2
numbers["three"] = 3

numbers
# {'ONE': 1, 'TWO': 2, 'THREE': 3}

numbers.update({"four": 4})
numbers
# {'ONE': 1, 'TWO': 2, 'THREE': 3, 'four': 4}

numbers.setdefault("five", 5)
# 5
numbers
# {'ONE': 1, 'TWO': 2, 'THREE': 3, 'four': 4, 'five': 5}
