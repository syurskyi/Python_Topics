'''

Given the provided cars dictionary:

Get all Jeeps
Get the first car of every manufacturer.
Get all vehicles containing the string Trail in their names (should work for other grep too)
Sort the models (values) alphabetically
See the docstrings and tests for more details. Have fun!

Update 18th of Sept 2018: as concluded in the forum it is better to pass the cars dict into each function to make its scope local.

cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}


def get_all_jeeps(cars=cars):
    """return a comma  + space (', ') separated string of jeep models (original order)"""
    pass


def get_first_model_each_manufacturer(cars=cars):
    """return a list of matching models (original ordering)"""
    pass


def get_all_matching_models(cars=cars, grep='trail'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    pass


def sort_car_models(cars=cars):
    """sort the car models (values) and return the resulting cars dict"""
    pass
'''


cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}


def get_all_jeeps(cars=cars):
    """return a comma  + space (', ') separated string of jeep models (original order)"""
    r = ', '.join(cars['Jeep'])
    return r

def get_first_model_each_manufacturer(cars=cars):
    """return a list of matching models (original ordering)"""
    r = []
    for key, value in cars.items():
        r.append(value[0])
    return r


def get_all_matching_models(cars=cars, grep='trail'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    r = []
    for key, value in cars.items():
        for c in value:
            if grep.lower() in c.lower():
                r.append(c)
    r.sort()
    return r




def sort_car_models(cars=cars):
    """sort the car models (values)  and return the resulting cars dict"""
    for key, value in cars.items():
        value.sort()
    return cars

get_all_jeeps(cars)
get_first_model_each_manufacturer(cars)
get_all_matching_models(cars)
sort_car_models(cars)