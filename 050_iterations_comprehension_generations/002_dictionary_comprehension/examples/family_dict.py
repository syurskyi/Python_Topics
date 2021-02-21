my_family = {'sister': {'name': 'Krista', 'age': 42}, 'mother': {'name': 'Cathie', 'age': 70}}

for key, value in my_family.items():
   family = {value['name']+" is my "+key+" and is "+str(value['age'])+" years old." for key, value in my_family.items()}
   print(family)
# {'Krista is my sister and is 42 years old.', 'Cathie is my mother and is 70 years old.'}
