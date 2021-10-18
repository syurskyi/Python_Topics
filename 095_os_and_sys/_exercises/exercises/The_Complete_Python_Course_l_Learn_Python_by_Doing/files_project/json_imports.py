______ json

file _ o..('friends_json.txt', 'r')
file_contents _ json.load(file)  # reads file and turns it to dictionary

file.close()

print(file_contents['friends'][0])

cars _ [
    {'make': 'Ford', 'model': 'Fiesta'},
    {'make': 'Ford', 'model': 'Focus'}
]

file _ o..('cars_json.txt', 'w')
json.dump(cars, file)
file.close()

my_json_string _ '[{"name": "Alfa Romeo", "released": 1950}]'

incorrect_car _ json.loads(my_json_string)
print(incorrect_car[0]['name'])
