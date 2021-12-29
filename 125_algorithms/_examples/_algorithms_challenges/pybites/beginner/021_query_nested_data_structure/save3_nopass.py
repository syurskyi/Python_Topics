cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}


def get_all_jeeps(cars=cars):
    """return a comma  + space (', ') separated string of jeep models
       (original order)"""
    jeeps = cars["Jeep"]
    return ", ".join(jeeps)


def get_first_model_each_manufacturer(cars=cars):
    """return a list of matching models (original ordering)"""
    first_model = []
    for model in cars.values():
        first_model.append(model[0])
    return first_model


def get_all_matching_models(cars=cars, grep='trail'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    cars_to_return = []
    for car_type in cars.values():
        for model in car_type:
            if grep.lower() in model.lower():
                cars_to_return.append(model)
    return cars_to_return



def sort_car_models(cars=cars):
    """return a copy of the cars dict with the car models (values)
       sorted alphabetically"""
    return dict((sorted(car_type), sorted(model)) for car_type, model in cars.items())