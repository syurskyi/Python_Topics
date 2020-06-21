# -*- coding: utf-8 -*-

import json

# Encoding and Decoding Custom Python Objects
# What happens when we try to serialize the Elf class from that Dungeons & Dragons app you’re working on?


class Elf:
    def __init__(self, level, ability_scores=None):
        self.level = level
        self.ability_scores = {
            "str": 11, "dex": 12, "con": 10,
            "int": 16, "wis": 14, "cha": 13
        } if ability_scores is None else ability_scores
        self.hp = 10 + self.ability_scores["con"]

# Not so surprisingly, Python complains that Elf isn’t serializable (which you’d know if you’ve ever tried to tell an
# Elf otherwise):
#
elf = Elf(level=4)
json.dumps(elf)
# TypeError: Object of type 'Elf' is not JSON serializable
# Although the json module can handle most built-in Python types, it doesn’t understand how to encode customized data
# types by default. It’s like trying to fit a square peg in a round hole—you need a buzzsaw and parental supervision.
#
# Simplifying Data Structures
# Now, the question is how to deal with more complex data structures. Well, you could try to encode and decode the JSON
# by hand, but there’s a slightly more clever solution that’ll save you some work. Instead of going straight from
# the custom data type to JSON, you can throw in an intermediary step.
# All you need to do is represent your data in terms of the built-in types json already understands. Essentially, you
# translate the more complex object into a simpler representation, which the json module then translates into JSON.
# It’s like the transitive property in mathematics: if A = B and B = C, then A = C.
# To get the hang of this, you’ll need a complex object to play with. You could use any custom class you like,
# but Python has a built-in type called complex for representing complex numbers, and it isn’t serializable by default.
# So, for the sake of these examples, your complex object is going to be a complex object. Confused yet?
#
z = 3 + 8j
print(type(z))
# <class 'complex'>
print(json.dumps(z))
# TypeError: Object of type 'complex' is not JSON serializable
# Where do complex numbers come from? You see, when a real number and an imaginary number love each other very much,
# they add together to produce a number which is (justifiably) called complex.
# A good question to ask yourself when working with custom types is What is the minimum amount of information necessary
# to recreate this object? In the case of complex numbers, you only need to know the real and imaginary parts,
# both of which you can access as attributes on the complex object:
#
print(z.real)
# 3.0
print(z.imag)
# 8.0
# Passing the same numbers into a complex constructor is enough to satisfy the __eq__ comparison operator:

print(complex(3, 8) == z)
# True

# Breaking custom data types down into their essential components is critical to both the serialization
# and deserialization processes.
# Encoding Custom Types
# To translate a custom object into JSON, all you need to do is provide an encoding function to the dump() method’s
# default parameter. The json module will call this function on any objects that aren’t natively serializable.
# Here’s a simple decoding function you can use for practice:
#
def encode_complex(z):
    if isinstance(z, complex):
        return (z.real, z.imag)
    else:
        type_name = z.__class__.__name__
        raise TypeError(f"Object of type '{type_name}' is not JSON serializable")

# Notice that you’re expected to raise a TypeError if you don’t get the kind of object you were expecting. This way,
# you avoid accidentally serializing any Elves. Now you can try encoding complex objects for yourself!

print(json.dumps(9 + 5j, default=encode_complex))
# '[9.0, 5.0]'
# json.dumps(elf, default=encode_complex)
# TypeError: Object of type 'Elf' is not JSON serializable
# Why did we encode the complex number as a tuple? Great question! That certainly wasn’t the only choice, nor is it
# necessarily the best choice. In fact, this wouldn’t be a very good representation if you ever wanted to decode
# the object later, as you’ll see shortly.
# The other common approach is to subclass the standard JSONEncoder and override its default() method:

class ComplexEncoder(json.JSONEncoder):
    def default(self, z):
        if isinstance(z, complex):
            return (z.real, z.imag)
        else:
            return super().default(z)

# Instead of raising the TypeError yourself, you can simply let the base class handle it. You can use this either
# directly in the dump() method via the cls parameter or by creating an instance of the encoder and calling its
# encode() method:
#
print(json.dumps(2 + 5j, cls=ComplexEncoder))
# '[2.0, 5.0]'

encoder = ComplexEncoder()
print(encoder.encode(3 + 6j))
# '[3.0, 6.0]'
#
# Decoding Custom Types
# While the real and imaginary parts of a complex number are absolutely necessary, they are actually not
# quite sufficient to recreate the object. This is what happens when you try encoding a complex number with
# the ComplexEncoder and then decoding the result:
#
complex_json = json.dumps(4 + 17j, cls=ComplexEncoder)
print(json.loads(complex_json))
# [4.0, 17.0]

# All you get back is a list, and you’d have to pass the values into a complex constructor if you wanted that complex
# object again. Recall our discussion about teleportation. What’s missing is metadata, or information about the type
# of data you’re encoding.
# I suppose the question you really ought ask yourself is What is the minimum amount of information that is
# both necessary and sufficient to recreate this object?
# The json module expects all custom types to be expressed as objects in the JSON standard. For variety, you can create
# a JSON file this time called complex_data.json and add the following object representing a complex number:

{
    "__complex__": True,
    "real": 42,
    "imag": 36
}
# See the clever bit? That "__complex__" key is the metadata we just talked about. It doesn’t really matter what
# the associated value is. To get this little hack to work, all you need to do is verify that the key exists:

def decode_complex(dct):
    if "__complex__" in dct:
        return complex(dct["real"], dct["imag"])
    return dct

# If "__complex__" isn’t in the dictionary, you can just return the object and let the default decoder deal with it.
# Every time the load() method attempts to parse an object, you are given the opportunity to intercede before
# the default decoder has its way with the data. You can do this by passing your decoding function to the object_hook parameter.
# Now play the same kind of game as before:
#
with open("complex_data.json") as complex_data:
    data = complex_data.read()
    z = json.loads(data, object_hook=decode_complex)
# ...
print(type(z))
# <class 'complex'>
# While object_hook might feel like the counterpart to the dump() method’s default parameter, the analogy really begins
# and ends there.
# This doesn’t just work with one object either. Try putting this list of complex numbers into complex_data.json and
# running the script again:

[
  {
    "__complex__":true,
    "real":42,
    "imag":36
  },
  {
    "__complex__":true,
    "real":64,
    "imag":11
  }
]
# If all goes well, you’ll get a list of complex objects:

with open("complex_data.json") as complex_data:
    data = complex_data.read()
    numbers = json.loads(data, object_hook=decode_complex)
# ...
print(numbers)
# [(42+36j), (64+11j)]

# You could also try subclassing JSONDecoder and overriding object_hook, but it’s better to stick with the lightweight
# solution whenever possible.
#
# All done!
# Congratulations, you can now wield the mighty power of JSON for any and all of your nefarious Python needs.
# While the examples you’ve worked with here are certainly contrived and overly simplistic, they illustrate a workflow
# you can apply to more general tasks:
#
# Import the json package.
# Read the data with load() or loads().
# Process the data.
# Write the altered data with dump() or dumps().
# What you do with your data once it’s been loaded into memory will depend on your use case. Generally, your goal will
# be gathering data from a source, extracting useful information, and passing that information along or keeping
# a record of it.
# Today you took a journey: you captured and tamed some wild JSON, and you made it back in time for supper!
# As an added bonus, learning the json package will make learning pickle and marshal a snap.
#
# Good luck with all of your future Pythonic endeavors!
