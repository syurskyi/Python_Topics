#Store the dict to a json file

_______ json

d  {"employees":[{"firstName": "John", "lastName": "Doe"},
                {"firstName": "Anna", "lastName": "Smith"},
                {"firstName": "Peter", "lastName": "Jones"}],
"owners":[{"firstName": "Jack", "lastName": "Petter"},
          {"firstName": "Jessy", "lastName": "Petter"}]}

with open("company1.json", "w") __ file:
    json.dump(d, file, indent4, sort_keysTrue)
