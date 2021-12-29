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
    jeeps = cars["Jeep"]
    r.. ", ".join(jeeps)


___ get_first_model_each_manufacturer(cars=cars):
    """return a list of matching models (original ordering)"""
    first_model    # list
    ___ model __ cars.values():
        first_model.a..(model[0])
    r.. first_model


___ get_all_matching_models(cars=cars, grep='trail'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    cars_to_return    # list
    ___ car_type __ cars.values():
        ___ model __ car_type:
            __ grep.lower() __ model.lower():
                cars_to_return.a..(model)
    r.. cars_to_return



___ sort_car_models(cars=cars):
    """return a copy of the cars dict with the car models (values)
       sorted alphabetically"""
    r.. d..((s..(car_type), s..(model)) ___ car_type, model __ cars.items())