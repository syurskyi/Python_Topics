#Store the dict to a json file

______ ____

d _ {"employees":[{"firstName": "John", "lastName": "Doe"},
                {"firstName": "Anna", "lastName": "Smith"},
                {"firstName": "Peter", "lastName": "Jones"}],
"owners":[{"firstName": "Jack", "lastName": "Petter"},
          {"firstName": "Jessy", "lastName": "Petter"}]}

w__ o..("company1.json", _) __ file:
    ____.d..(d, file, indent_4, sort_keys_True)
