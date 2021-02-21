my_family = {
  "sister": {
    "name": "Suzy",
    "age": 32
  },
  "father": {
    "name": "John",
    "age": 55
  },
  "brother": {
    "name": "Billy",
    "age": 21
  }
}

family_stuff = set()

for family_member, member_values in my_family.items():
  family_stuff.add(f'{member_values["name"]} is my {family_member} and is {str(member_values["age"])} years old.')

print(family_stuff)

more_family_stuff = {f'{member_values["name"]} is my {family_member} and is {str(member_values["age"])} years old.'
  for (family_member, member_values) in my_family.items()
  }

print(more_family_stuff)