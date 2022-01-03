# ____ i.. _______ c__
#
# cars = {
#     'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
#     'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
#     'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
#     'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
#     'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
# }
#
#
# ___ get_all_jeeps cars=cars
#     """return a comma  + space (', ') separated string of jeep models
#        (original order)"""
#     r.. ', '.j.. ? 'Jeep'
#
#
# ___ get_first_model_each_manufacturer cars=cars
#     """return a list of matching models (original ordering)"""
#     r.. models 0 ___ ? __ cars.v..
#
#
# ___ get_all_matching_models cars=cars, grep='trail'
#     """return a list of all models containing the case insensitive
#        'grep' string which defaults to 'trail' for this exercise,
#        sort the resulting sequence alphabetically"""
#     grep  ?.l..
#     # flatten list of lists (less obvious way: "sum(cars.values(), [])")
#     models  l.. c__.f..(cars.v..
#     matching_models  [model ___ ? __ ?
#                        __ ? __ ?.l..]
#     r.. s.. ?
#
#
# ___ sort_car_models cars=cars
#     """return a copy of the cars dict with the car models (values)
#        sorted alphabetically"""
#     r.. manufacturer: s.. m.. ___
#             ? ? __ ?.i..