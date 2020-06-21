fields = ['name', 'last_name', 'age', 'job']
values = ['John', 'Doe', '45', 'Python Developer']

a_dict = dict(zip(fields, values))
a_dict

# {'name': 'John', 'last_name': 'Doe', 'age': '45', 'job': 'Python Developer'}

new_job = ['Python Consultant']
field = ['job']
a_dict.update(zip(field, new_job))
a_dict
# {'name': 'John', 'last_name': 'Doe', 'age': '45', 'job': 'Python Consultant'}