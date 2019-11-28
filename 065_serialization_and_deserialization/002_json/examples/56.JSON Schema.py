print('#' * 52 + '  We can start with a simple schema as follows:')

person_schema = {
    "type": "object",
    "properties": {
        "firstName": {"type": "string"},
        "middleInitial": {"type": "string"},
        "lastName": {"type": "string"},
        "age": {"type": "number"}
    }
}

p1 = '''
    {
        "firstName": "John",
        "middleInitial": "M",
        "lastName": "Cleese",
        "age": 79
    }
'''

p2 = '''
    {
        "firstName": "John",
        "middleInitial": 100,
        "lastName": "Cleese",
        "age": "Unknown"
    }
'''

p3 = '''
    {
        "firstName": "John",
        "age": -10.5
    }
'''


person_schema = {
    "type": "object",
    "properties": {
        "firstName": {
            "type": "string",
            "minLength": 1
        },
        "middleInitial": {
            "type": "string",
            "minLength": 1,
            "maxLength": 1
        },
        "lastName": {
            "type": "string",
            "minLength": 1
        },
        "age": {
            "type": "integer",
            "minimum": 0
        }
    },
    "required": ["firstName", "lastName"]
}

person_schema = {
    "type": "object",
    "properties": {
        "firstName": {
            "type": "string",
            "minLength": 1
        },
        "middleInitial": {
            "type": "string",
            "minLength": 1,
            "maxLength": 1
        },
        "lastName": {
            "type": "string",
            "minLength": 1
        },
        "age": {
            "type": "integer",
            "minimum": 0
        },
        "eyeColor": {
            "type": "string",
            "enum": ["amber", "blue", "brown", "gray",
                     "green", "hazel", "red", "violet"]
        }
    },
    "required": ["firstName", "lastName"]
}

from jsonschema import validate
from jsonschema.exceptions import ValidationError
from json import loads, dumps, JSONDecodeError

print(p1)

try:
    validate(loads(p1), person_schema)
except JSONDecodeError as ex:
    print(f'Invalid JSON: {ex}')
except ValidationError as ex:
    print(f'Validation error: {ex}')
else:
    print('JSON is valid')

print(p2)

try:
    validate(loads(p2), person_schema)
except JSONDecodeError as ex:
    print(f'Invalid JSON: {ex}')
except ValidationError as ex:
    print(f'Validation error: {ex}')
else:
    print('JSON is valid')

print(p3)
try:
    validate(loads(p3), person_schema)
except JSONDecodeError as ex:
    print(f'Invalid JSON: {ex}')
except ValidationError as ex:
    print(f'Validation error: {ex}')
else:
    print('JSON is valid')

print('#' * 52 + '  You will notice that the validator only returns the first validation error it encounters.')
print('#' * 52 + '  This can be changed to run the entire validation and return all the validation errors (if any), '
                 '  but utilizes a slightly different way of performing validation:')

from jsonschema import Draft4Validator

validator = Draft4Validator(person_schema)

for error in validator.iter_errors(loads(p2)):
    print(error, end='\n-----------\n')

print('#' * 52 + '  We can also test out the schema for `eyeColor`:')

p4 = '''
    {
        "firstName": "John",
        "middleInitial": null,
        "lastName": "Cleese",
        "eyeColor": "blue-gray"
    }
'''

for error in validator.iter_errors(loads(p4)):
    print(error, end='\n-----------\n')

