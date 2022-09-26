# spelling_dict.py

from collections import UserDict

UK_TO_US = {"colour": "color", "flavour": "flavor", "behaviour": "behavior"}

class EnglishSpelledDict(UserDict):
    def __getitem__(self, key):
        try:
            return self.data[key]
        except KeyError:
            pass
        try:
            return self.data[UK_TO_US[key]]
        except KeyError:
            pass
        raise KeyError(key)

    def __setitem__(self, key, value):
        try:
            key = UK_TO_US[key]
        except KeyError:
            pass
        self.data[key] = value

# from spelling_dict import EnglishSpelledDict

likes = EnglishSpelledDict({"color": "blue", "flavour": "vanilla"})

likes
# {'color': 'blue', 'flavor': 'vanilla'}

likes["flavour"]
# vanilla
likes["flavor"]
# vanilla

likes["behaviour"] = "polite"
likes
# {'color': 'blue', 'flavor': 'vanilla', 'behavior': 'polite'}

likes.get("colour")
# 'blue'
likes.get("color")
# 'blue'

likes.update({"behaviour": "gentle"})
likes
# {'color': 'blue', 'flavor': 'vanilla', 'behavior': 'gentle'}
