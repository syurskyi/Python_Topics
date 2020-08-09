cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}


___ get_all_jeeps(cars=cars
    """return a comma  + space (', ') separated string of jeep models
       (original order)"""
    r_ ', '.join(cars['Jeep'])


___ get_first_model_each_manufacturer(cars=cars
    """return a list of matching models (original ordering)"""
    r_ [x[1][0] for x in cars.items()]


___ get_all_matching_models(cars=cars, grep='trail'
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    r_ sorted([x for y in cars.items() for x in y[1] __ grep.lower() in x.lower()])


___ sort_car_models(cars=cars
    """return a copy of the cars dict with the car models (values)
       sorted alphabetically"""
    r_ dict(sorted([(x[0], sorted(x[1])) for x in cars.items()]))
