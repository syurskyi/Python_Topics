# upper_dict.py

class UpperCaseDict(dict):
    def __init__(self, mapping=None, /, **kwargs):
        if mapping is not None:
            mapping = {
                str(key).upper(): value for key, value in mapping.items()
            }
        else:
            mapping = {}
        if kwargs:
            mapping.update(
                {str(key).upper(): value for key, value in kwargs.items()}
            )
        super().__init__(mapping)

    def __setitem__(self, key, value):
        key = key.upper()
        super().__setitem__(key, value)

# from upper_dict import UpperCaseDict

numbers = UpperCaseDict({"one": 1, "two": 2, "three": 3})
numbers
# {'ONE': 1, 'TWO': 2, 'THREE': 3}

numbers.update({"four": 4})
numbers
# {'ONE': 1, 'TWO': 2, 'THREE': 3, 'four': 4}
