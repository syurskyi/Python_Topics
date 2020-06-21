# -*- coding: utf-8 -*-

# A Simple Serialization Example
# Imagine you’re working with a Python object in memory that looks a little something like this:

data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian"
    }
}
# It is critical that you save this information to disk, so your mission is to write it to a file.
#
# Using Python’s context manager, you can create a file called data_file.json and open it in write mode.
# (JSON files conveniently end in a .json extension.)

import json

with open("data_file.json", "w") as write_file:
    json.dump(data, write_file)
# Note that dump() takes two positional arguments: (1) the data object to be serialized, and (2) the file-like object
# to which the bytes will be written.
# Or, if you were so inclined as to continue using this serialized JSON data in your program, you could write it
# to a native Python str object.
#
json_string = json.dumps(data)
# Notice that the file-like object is absent since you aren’t actually writing to disk. Other than that, dumps() is just
# like dump().
# Hooray! You’ve birthed some baby JSON, and you’re ready to release it out into the wild to grow big and strong.
#
# Some Useful Keyword Arguments
# Remember, JSON is meant to be easily readable by humans, but readable syntax isn’t enough if it’s
# all squished together. Plus you’ve probably got a different programming style than me, and it might be easier for you
# to read code when it’s formatted to your liking.
# NOTE: Both the dump() and dumps() methods use the same keyword arguments.
# The first option most people want to change is whitespace. You can use the indent keyword argument to specify
# the indentation size for nested structures. Check out the difference for yourself by using data, which we defined
# above, and running the following commands in a console:
#
print(json.dumps(data))
print(json.dumps(data, indent=4))
# Another formatting option is the separators keyword argument. By default, this is a 2-tuple of the separator strings
# (", ", ": "), but a common alternative for compact JSON is (",", ":"). Take a look at the sample JSON again to see
# where these separators come into play.
# There are others, like sort_keys, but I have no idea what that one does. You can find a whole list in the docs if
# you’re curious.
