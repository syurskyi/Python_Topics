#Store the dict to a json file

______ json

d _ {"employees":[{"firstName": "John", "lastName": "Doe"},
                {"firstName": "Anna", "lastName": "Smith"},
                {"firstName": "Peter", "lastName": "Jones"}],
"owners":[{"firstName": "Jack", "lastName": "Petter"},
          {"firstName": "Jessy", "lastName": "Petter"}]}

with open("company1.json", "w") as file:
    json.dump(d, file, indent_4, sort_keys_True)
