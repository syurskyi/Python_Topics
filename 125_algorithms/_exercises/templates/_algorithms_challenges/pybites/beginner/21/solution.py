____ itertools _______ chain

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
    r.. [models[0] ___ models __ cars.values()]


___ get_all_matching_models(cars=cars, grep='trail'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    grep = grep.lower()
    # flatten list of lists (less obvious way: "sum(cars.values(), [])")
    models = l..(chain.from_iterable(cars.values()))
    matching_models = [model ___ model __ models
                       __ grep __ model.lower()]
    r.. s..(matching_models)


___ sort_car_models(cars=cars):
    """return a copy of the cars dict with the car models (values)
       sorted alphabetically"""
    r.. {manufacturer: s..(models) ___
            manufacturer, models __ cars.items()}