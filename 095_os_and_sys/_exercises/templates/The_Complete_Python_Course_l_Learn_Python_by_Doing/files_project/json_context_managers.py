______ json

w__ o..('friends_json.txt', 'r') __ file:
    file_contents = json.load(file)  # reads file and turns it to dictionary

print(file_contents['friends'][0])


cars = [
    {'make': 'Ford', 'model': 'Fiesta'},
    {'make': 'Ford', 'model': 'Focus'}
]

w__ o..('cars_json.txt', 'w') __ file:
    json.dump(cars, file)


my_json_string = '[{"name": "Alfa Romeo", "released": 1950}]'

incorrect_car = json.loads(my_json_string)
print(incorrect_car[0]['name'])
