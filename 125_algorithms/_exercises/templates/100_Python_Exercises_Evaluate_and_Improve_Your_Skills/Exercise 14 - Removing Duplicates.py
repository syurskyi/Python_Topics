#Write a script that remove duplicates from a list
a _ ["1", 1, "1", 2]
a _ li..(set(a))
print(a)

#If you want to keep the order, you need OrderedDict
from collections ______ OrderedDict
a _ ["1", 1, "1", 2]
a _ li..(OrderedDict.fromkeys(a))
print(a)
