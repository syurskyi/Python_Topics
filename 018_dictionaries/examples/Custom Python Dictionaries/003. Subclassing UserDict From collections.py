from collections import UserDict

class UpperCaseDict(UserDict):
    def __setitem__(self, key, value):
        key = key.upper()
        super().__setitem__(key, value)


numbers = UpperCaseDict({"one": 1, "two": 2})

numbers["three"] = 3
numbers.update({"four": 4})
numbers.setdefault("five", 5)
# 5

numbers
# {'ONE': 1, 'TWO': 2, 'THREE': 3, 'FOUR': 4, 'FIVE': 5}
