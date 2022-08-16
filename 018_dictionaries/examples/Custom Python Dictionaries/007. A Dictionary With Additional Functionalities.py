# extended_dict.py

class ExtendedDict(dict):
    def apply(self, action):
        for key, value in self.items():
            self[key] = action(value)

    def remove(self, key):
        del self[key]

    def is_empty(self):
        return len(self) == 0

# from extended_dict import ExtendedDict

numbers = ExtendedDict({"one": 1, "two": 2, "three": 3})
numbers
# {'one': 1, 'two': 2, 'three': 3}

numbers.apply(lambda x: x**2)
numbers
# {'one': 1, 'two': 4, 'three': 9}

numbers.remove("two")
numbers
# {'one': 1, 'three': 9}

numbers.is_empty()
# False
