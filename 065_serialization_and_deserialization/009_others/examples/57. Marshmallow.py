class Person:
    def __init__(self, first_name, last_name, dob):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob

    def __repr__(self):
        return f'Person({self.first_name}, {self.last_name}, {self.dob})'

from datetime import date

p1 = Person('John', 'Cleese', date(1939, 10, 27))

print(p1)

print('#' * 52 + '  So we want to serialize and deserialize this `Person` object into a simple dictionary'
                 '  containing strings, including an ISO formatted string for the date of birth.')

from marshmallow import Schema, fields


class PersonSchema(Schema):
    first_name = fields.Str()
    last_name = fields.Str()
    dob = fields.Date()


person_schema = PersonSchema()
print(person_schema.dump(p1))

print('#' * 52 + '  As you can see we have two properties here: `data` and `errors`.')
print('#' * 52 + '  The `data` property will contain our serialized data, and the `errors` property will tell us'
                 '  if any errors were encountered while serializing our objects.')

print(type(person_schema.dump(p1).data))

print('#' * 52 + '  We can also serialize our objects directly to JSON using `dumps`:')

print(person_schema.dumps(p1).data)

print('#' * 52 + '  We can use other objects, not necessarily of `Person` type, '
                 '  and if those fields are present they will be used in the serialization:')

from collections import namedtuple

PT = namedtuple('PT', 'first_name, last_name, dob')

p2 = PT('Eric', 'Idle', date(1943, 3, 29))

print(person_schema.dumps(p2).data)

print('#' * 52 + '  But if we use an object that does not have the required fields:')

PT2 = namedtuple('PT2', 'first_name, last_name, age')
p3 = PT2('Michael', 'Palin', 75)

print(person_schema.dumps(p3).data)

print('#' * 52 + '  As you can see Marshmallow here only uses what it can.')
print('#' * 52 + '  Whats interesting is that we can also specify what fields should occur in the deserialized output, '
                 '  using `only` to specify inclusions, or `exclude` to specify exclusions:')

person_partial = PersonSchema(only=('first_name', 'last_name'))
print(person_partial.dumps(p1).data)

print('#' * 52 + '  Equivalently:')

person_partial = PersonSchema(exclude=['dob'])

print(person_partial.dumps(p1).data)

print('#' * 52 + '  What happens if we have the wrong data type for those fields?')

p4 = Person(100, None, 200)
print(person_schema.dumps(p4))

print('#' * 52 + '  ')


class Movie:
    def __init__(self, title, year, actors):
        self.title = title
        self.year = year
        self.actors = actors


class MovieSchema(Schema):
    title = fields.Str()
    year = fields.Integer()
    actors = fields.Nested(PersonSchema, many=True)


print(p1, p2)

parrot = Movie('Parrot Sketch', 1989, [p1,
                                       Person('Michael',
                                              'Palin',
                                              date(1943, 5, 5))
                                      ])
print(MovieSchema().dumps(parrot))

print('#' * 52 + '  To deserialize a simple dictionary we use the `load` method (deserializes a dictionary,'
                 '  the opposite of what `dump` does basically).')
print('#' * 52 + '  We deserialize a JSON string using the `loads` metho')
print('#' * 52 + '  Lets recall our Person schema:')


class PersonSchema(Schema):
    first_name = fields.Str()
    last_name = fields.Str()
    dob = fields.Date()


person_schema = PersonSchema()
print(person_schema.load(dict(first_name='John',
                              last_name='Cleese',
                              dob='1939-10-27')))

print('#' * 52 + '  So you can see we get this `UnmarshalResult` object back, with a `data` property - '
                 '  notice how the data was converted from a string into an actual date object.')
print('#' * 52 + '  But we still did not get a `Person` object back in `data`. Instead we got a plain dictionary back -'
                 '  ultimately we may want a `Person` object.')
print('#' * 52 + '  To do this, we need to tell Marshmallow what object to use when it deserializes our data:')

from marshmallow import post_load


class PersonSchema(Schema):
    first_name = fields.Str()
    last_name = fields.Str()
    dob = fields.Date()

    @post_load
    def make_person(self, data):
        return Person(**data)


person_schema = PersonSchema()

print(person_schema.load(dict(first_name='John',
                              last_name='Cleese',
                              dob='1939-10-27')))

print('#' * 52 + '  And now you can see that `data` contains a `Person` object.')
print('#' * 52 + '  So now lets go ahead and fix up our `MovieSchema` as well:')


class MovieSchema(Schema):
    title = fields.Str()
    year = fields.Integer()
    actors = fields.Nested(PersonSchema, many=True)

    @post_load
    def make_movie(self, data):
        return Movie(**data)


movie_schema = MovieSchema()

json_data = '''
{"actors": [
    {"first_name": "John", "last_name": "Cleese", "dob": "1939-10-27"}, 
    {"first_name": "Michael", "last_name": "Palin", "dob": "1943-05-05"}], 
"title": "Parrot Sketch", 
"year": 1989}
'''

movie = movie_schema.loads(json_data).data

print(type(movie))

print(movie.title, movie.year)

print(movie.actors)
