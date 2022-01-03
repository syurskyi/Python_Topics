____ i.. _______ c__

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
    ___ car __ cars['Jeep']:
        __ car != cars['Jeep'][0]:
            cars_str += ', '
        cars_str += car
    r.. cars_str


___ get_first_model_each_manufacturer(cars=cars):
    """return a list of matching models (original ordering)"""
    carlist    # list
    ___ car __ cars:
        #print(car)
        carlist.a..(cars[car][0])
    r.. carlist


___ get_all_matching_models(cars=cars, grep='trail'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    greplist    # list
    ___ car __ cars:
        ___ model __ cars[car]:
            __ grep.upper() __ model.upper():
                greplist.a..(model)
    r.. s..(greplist)


___ sort_car_models(cars=cars):
    """return a copy of the cars dict with the car models (values)
       sorted alphabetically"""
    newdict    # dict
    ___ car __ cars:
        newdict[car] = s..(cars[car])
    r.. newdict


print(l..(c__.f..(cars.values())))
