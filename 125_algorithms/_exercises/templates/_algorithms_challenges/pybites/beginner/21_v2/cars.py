_______ re

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


    result    # list


    ___ value __ cars.values():
        result.a..(value[0])

    r.. result



___ get_all_matching_models(cars=cars, grep='trail'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    result    # list
    

    regex = re.compile(grep,flags=re.I)

    ___ value __ cars.values():
        ___ car __ value:
            __ regex.search(car):
                result.a..(car)
    
    result.s..()
    r.. result


___ sort_car_models(cars=cars):
    """return a copy of the cars dict with the car models (values)
       sorted alphabetically"""
    

    copy = {} 
    ___ key,value __ cars.items():
        copy[key] = s..(value)

    
    r.. copy







