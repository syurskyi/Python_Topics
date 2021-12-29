from itertools import chain

cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}


___ get_all_jeeps(cars=cars):
    """return a comma  + space (', ') separated string of jeep models
       (original order)"""
    cars_str = ''
    for car in cars['Jeep']:
        __ car != cars['Jeep'][0]:
            cars_str += ', '
        cars_str += car
    return cars_str


___ get_first_model_each_manufacturer(cars=cars):
    """return a list of matching models (original ordering)"""
    carlist = []
    for car in cars:
        #print(car)
        carlist.append(cars[car][0])
    return carlist


___ get_all_matching_models(cars=cars, grep='trail'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    greplist = []
    for car in cars:
        for model in cars[car]:
            __ grep.upper() in model.upper():
                greplist.append(model)
    return sorted(greplist)


___ sort_car_models(cars=cars):
    """return a copy of the cars dict with the car models (values)
       sorted alphabetically"""
    newdict = {}
    for car in cars:
        newdict[car] = sorted(cars[car])
    return newdict


print(list(chain.from_iterable(cars.values())))
