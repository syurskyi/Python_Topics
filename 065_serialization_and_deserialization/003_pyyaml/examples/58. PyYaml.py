# YAML Format
# YAML, like JSON, is another data serialization standard. It is actually easier to read than JSON, and although it has
# been around for a long time (since 2001), it has gained a lot of popularity, especially in the Dev Ops world for
# configuration files (Docker, Kubernetes, etc).
# Like JSON it is able to represent simple data types (strings, numbers, boolean, etc) as well as collections and
# associative arrays (dictionaries).
# YAML focuses on human readability, and is a little more complex to parse.
# Here is a sample YAML file:
# title: Parrot Sketch
# year: 1989
# actors:
#     - first_name: John
#       last_name: Cleese
#       dob: 1939-10-27
#     - first_name: Michael
#       last_name: Palin
#       dob: 1943-05-05
# As you can see this is much easier to read than JSON or XML.
# To parse YAML into a Python dictionary would take a fair amount of work - especially since YAML is quite flexible.
# Fortunately, we can use the 3rd party library, pyyaml to do this for us.
# Again, I'm only going to show you a tiny bit of this library, and you can read more about it here:
# https://pyyaml.org/wiki/PyYAMLDocumentation
# (It's definitely less of a learning curve than Marshmallow!!)
# Caution
# When you load a yaml file using pyyaml, be careful - like pickling it can actually call out to Python functions - 
# so do not load untrusted YAML files using pyyaml!

import yaml

data = '''
---
title: Parrot Sketch
year: 1989
actors:
    - first_name: John
      last_name: Cleese
      dob: 1939-10-27
    - first_name: Michael
      last_name: Palin
      dob: 1943-05-05
'''

d = yaml.load(data)

print(type(d))
# dict

from pprint import pprint
pprint(d)
# {'actors': [{'dob': datetime.date(1939, 10, 27),
#              'first_name': 'John',
#              'last_name': 'Cleese'},
#             {'dob': datetime.date(1943, 5, 5),
#              'first_name': 'Michael',
#              'last_name': 'Palin'}],
#  'title': 'Parrot Sketch',
#  'year': 1989}
# ######################################################################################################################

# You'll notice that unlike the built-in JSON parser, PyYAML was able to automatically deduce the date type in our YAML,
# as well of course as strings and integers.
# Of course, serialization works the same way:

print('#' * 52 + '  You will notice that unlike the built-in JSON parser, PyYAML was able to automatically deduce '
                 '  the `date` type in our YAML, as well of course as strings and integers.')

d = {'a': 100, 'b': False, 'c': 10.5, 'd': [1, 2, 3]}
print(yaml.dump(d))
# a: 100
# b: false
# c: 10.5
# d: [1, 2, 3]
#
# ######################################################################################################################

# You'll notice in the above example that the list was represented using [1, 2, 3] - this is valid YAML as well,
# and is equivalent to this notation:
#
# d:
#     - 1
#     - 2
#     - 3
# If you prefer this block style, you can force it this way:

print('#' * 52 + '  You will notice in the above example that the list was represented using `[1, 2, 3]` - '
                 '  this is valid YAML as well, and is equivalent to this notation:')
print('#' * 52 + '  If you prefer this block style, you can force it this way:')

print(yaml.dump(d, default_flow_style=False))
# a: 100
# b: false
# c: 10.5
# d:
# - 1
# - 2
# - 3
# ######################################################################################################################

# What's interesting about PyYAML is that it can also automatically serialize and deserialize complex objects:

print('#' * 52 + '  What is interesting about PyYAML is that it can also automatically'
                 '  serialize and deserialize complex objects:')


class Person:
    def __init__(self, name, dob):
        self.name = name
        self.dob = dob

    def __repr__(self):
        return f'Person(name={self.name}, dob={self.dob})'


from datetime import date

p1 = Person('John Cleese', date(1939, 10, 27))
p2 = Person('Michael Palin', date(1934, 5, 5))
print(yaml.dump({'john': p1, 'michael': p2}))
# john: !!python/object:__main__.Person {dob: 1939-10-27, name: John Cleese}
# michael: !!python/object:__main__.Person {dob: 1934-05-05, name: Michael Palin}
# ######################################################################################################################

# Notice that weird looking syntax? It's actually useful when we deserialize the YAML string - of course it means
# we must have a Person class defined with the appropriate init method.
print('#' * 52 + '  Notice that weird looking syntax? ')
print('#' * 52 + '  Its actually useful when we deserialize the YAML string - ')
print('#' * 52 + '  of course it means we must have a `Person` class defined with the appropriate init method.')

yaml_data = '''
john: !!python/object:__main__.Person 
    dob: 1939-10-27
    name: John Cleese
michael: !!python/object:__main__.Person 
    dob: 1934-05-05
    name: Michael Palin
'''

d = yaml.load(yaml_data)
print(d)
# {'john': Person(name=John Cleese, dob=1939-10-27),
#  'michael': Person(name=Michael Palin, dob=1934-05-05)}
# ######################################################################################################################

# As you can see, john and michael were deserialized into Person type objects.
# This is why you have to be quite careful with the source of any YAML you deserialize.
# Here's an evil example:

print('#' * 52 + '  As you can see, `john` and `michael` were deserialized into `Person` type objects.')
print('#' * 52 + '  This is why you have to be quite careful with the source of any YAML you deserialize.')

yaml_data = '''
exec_paths: 
    !!python/object/apply:os.get_exec_path []
exec_command:
    !!python/object/apply:subprocess.check_output [['ls', '/']]
'''

# yaml.load(yaml_data)
# {'exec_paths': ['/Users/fbaptiste/anaconda3/envs/deepdive/bin',
#   '/Users/fbaptiste/anaconda3/envs/deepdive/bin',
#   '/Users/fbaptiste/anaconda3/bin',
#   '/usr/local/bin',
#   '/usr/bin',
#   '/bin',
#   '/usr/sbin',
#   '/sbin'],
#  'exec_command': b'Applications\nLibrary\nNetwork\nSystem\nUsers\nVolumes\nbin\ncores\ndev\netc\nhome\ninstaller.failurerequests\nnet\nprivate\nsbin\ntmp\nusr\nvar\n'}
# ######################################################################################################################

# So, be very careful with load. In general it is safer practice to use the safe_load method instead,
# but you will lose the ability to deserialize into custom Python objects, unless you override that behavior.
# You can always use Marshmallow to do that secondary step in a safer way.

print('#' * 52 + '  So, be very careful with `load`.')
print('#' * 52 + '  In general it is safer practice to use the `safe_load` method instead,'
                 '  but you will lose the ability to deserialize into custom Python objects,'
                 '  unless you override that behavior.')
print('#' * 52 + '  You can always use Marshmallow to do that secondary step in a safer way.')

# yaml.safe_load(yaml_data) #  ConstructorError: could not determine a constructor for the tag
# ######################################################################################################################

# To override and allow certain Python objects to be deserialized in safe_load we can proceed this way.
# Firstly we are going to simplify the object tag notation by customizing it in our Person class, and we are also
# going to make our object as safe to be deserialized. Our Person class will now have to inherit from
# the yaml.YAMLObject:

print('#' * 52 + '  To override and allow certain Python objects to be deserialized in `safe_load`'
                 '  we can proceed this way.')

print('#' * 52 + '  Firstly we are going to simplify the object tag notation by customizing it in our `Person` class,'
                 '  and we are also going to make our object as safe to be deserialized.')
print('#' * 52 + '  Our `Person` class will now have to inherit from the `yaml.YAMLObject`:')

from yaml import YAMLObject, SafeLoader


class Person(YAMLObject):
    yaml_tag = '!Person'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'Person(name={self.name}, age={self.age})'

# First let's see how objects are now serialized:

print(yaml.dump(dict(john=Person('John Cleese', 79),
                     michael=Person('Michael Palin', 74))))
# 'john: !Person {age: 79, name: John Cleese}\nmichael: !Person {age: 74, name: Michael Palin}\n'
# ######################################################################################################################

# As you can see we have a slightly cleaner syntax.
# Now let's try to load the serialized version:

print('#' * 52 + '  As you can see we have a slightly cleaner syntax.')
print('#' * 52 + '  Now lets try to load the serialized version:')

yaml_data = '''
john: !Person
    name: John Cleese
    age: 79
michael: !Person
    name: Michael Palin
    age: 74
'''

# print(yaml.load(yaml_data))  #  ERROR need to check why I have error
# {'john': Person(name=John Cleese, age=79),
#  'michael': Person(name=Michael Palin, age=74)}
# ######################################################################################################################

# yaml.safe_load(yaml_data)
# ConstructorError: could not determine a constructor for the tag '!Person'
#   in "<unicode string>", line 2, column 7:
#     john: !Person
#           ^
# So now let's mark our Person object as safe:
# ######################################################################################################################

print('#' * 52 + '  So now lets mark our `Person` object as safe:')

class Person(YAMLObject):
    yaml_tag = '!Person'
    yaml_loader = SafeLoader

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'Person(name={self.name}, age={self.age})'

print(yaml.safe_load(yaml_data))
# {'john': Person(name=John Cleese, age=79),
#  'michael': Person(name=Michael Palin, age=74)}
# ######################################################################################################################

# And as you can see, the deserializtion now works for the Person class.
# There's a lot more this library can do, so look at the reference if you want to use YAML.
# Also, as I mentionmed before, you can combine this with Marshmallow for example to get to a full marshalling solution
# to complex (custom) Python types.
