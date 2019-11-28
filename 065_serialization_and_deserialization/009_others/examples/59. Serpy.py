print('#' * 52 + '  If you are just looking for deserialization, then `Serpy` might work for you. ')
print('#' * 52 + '  It is extremely fast, but only provides serialization.')


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'Person(name={self.name}, age={self.age})'

import serpy


class PersonSerializer(serpy.Serializer):
    name = serpy.StrField()
    age = serpy.IntField()


p1 = Person('Michael Palin', 75)

print(PersonSerializer(p1).data)


print('#' * 52 + '  Of course, we can get more complex schemas defined.')
print('#' * 52 + '  Lets implement a schema for our `Movie` example we did in a previous video on Marshmallow.')


class Movie:
    def __init__(self, title, year, actors):
        self.title = title
        self.year = year
        self.actors = actors


class MovieSerializer(serpy.Serializer):
    title = serpy.StrField()
    year = serpy.IntField()
    actors = PersonSerializer(many=True)


p2 = Person('John Cleese', 79)
movie = Movie('Parrot Sketch', 1989, [p1, p2])
print(movie.title, movie.year, movie.actors)
print(MovieSerializer(movie).data)

print('#' * 52 + '  Note that the result of serialization is to a basic Python dictionary,')
print('#' * 52 + '  and you can takes this further to JSON or YAML using the standard library '
                 ' `json` module or `PyYaml`.')

import json
import yaml

print(json.dumps(MovieSerializer(movie).data))

print(yaml.dump(MovieSerializer(movie).data,
                default_flow_style=False))
