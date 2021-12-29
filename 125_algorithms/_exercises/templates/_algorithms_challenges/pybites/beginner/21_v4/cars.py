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
    r.. ', '.join(cars['Jeep'])


___ get_first_model_each_manufacturer(cars=cars):
    """return a list of matching models (original ordering)"""
    r.. [x[1][0] ___ x __ cars.items()]


___ get_all_matching_models(cars=cars, grep='trail'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    r.. s..([x ___ y __ cars.items() ___ x __ y[1] __ grep.lower() __ x.lower()])


___ sort_car_models(cars=cars):
    """return a copy of the cars dict with the car models (values)
       sorted alphabetically"""
    r.. d..(s..([(x[0], s..(x[1])) ___ x __ cars.items()]))
