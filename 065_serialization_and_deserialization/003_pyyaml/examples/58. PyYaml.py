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

from pprint import pprint

pprint(d)

print('#' * 52 + '  You will notice that unlike the built-in JSON parser, PyYAML was able to automatically deduce '
                 '  the `date` type in our YAML, as well of course as strings and integers.')

d = {'a': 100, 'b': False, 'c': 10.5, 'd': [1, 2, 3]}

print(yaml.dump(d))

print('#' * 52 + '  You will notice in the above example that the list was represented using `[1, 2, 3]` - '
                 '  this is valid YAML as well, and is equivalent to this notation:')
print('#' * 52 + '  If you prefer this block style, you can force it this way:')

print(yaml.dump(d, default_flow_style=False))

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

print('#' * 52 + '  As you can see, `john` and `michael` were deserialized into `Person` type objects.')
print('#' * 52 + '  This is why you have to be quite careful with the source of any YAML you deserialize.')

yaml_data = '''
exec_paths: 
    !!python/object/apply:os.get_exec_path []
exec_command:
    !!python/object/apply:subprocess.check_output [['ls', '/']]
'''

# yaml.load(yaml_data)

print('#' * 52 + '  So, be very careful with `load`.')
print('#' * 52 + '  In general it is safer practice to use the `safe_load` method instead,'
                 '  but you will lose the ability to deserialize into custom Python objects,'
                 '  unless you override that behavior.')
print('#' * 52 + '  You can always use Marshmallow to do that secondary step in a safer way.')

# yaml.safe_load(yaml_data) #  ConstructorError: could not determine a constructor for the tag

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


print(yaml.dump(dict(john=Person('John Cleese', 79),
                     michael=Person('Michael Palin', 74))))

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

# yaml.safe_load(yaml_data)

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
