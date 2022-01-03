# ____ cars _______ (get_all_jeeps, get_first_model_each_manufacturer,
#                   get_all_matching_models, sort_car_models)
#
#
# ___ test_get_all_jeeps
#     expected  'Grand Cherokee, Cherokee, Trailhawk, Trackhawk'
#     actual ?
#     ... t.. ? __ s..
#     ... ? __ ?
#
#
# ___ test_get_first_model_each_manufacturer
#     actual ?
#     expected  ['Falcon', 'Commodore', 'Maxima', 'Civic', 'Grand Cherokee']
#     ... ? __ ?
#
#
# ___ test_get_all_matching_models_default_grep
#     expected  ['Trailblazer', 'Trailhawk']
#     ... ? __ ?
#
#
# ___ test_get_all_matching_models_different_grep
#     expected  ['Accord', 'Commodore', 'Falcon']
#     ... ? g..+'CO' __ ?
#
#
# ___ test_sort_dict_alphabetically
#     actual ?
#     # Order of keys should not matter, two dicts are equal if they have the
#     # same keys and the same values.
#     # The car models (values) need to be sorted here though
#     expected  {
#         'Ford': ['Fairlane', 'Falcon', 'Festiva', 'Focus'],
#         'Holden': ['Barina', 'Captiva', 'Commodore', 'Trailblazer'],
#         'Honda': ['Accord', 'Civic', 'Jazz', 'Odyssey'],
#         'Jeep': ['Cherokee', 'Grand Cherokee', 'Trackhawk', 'Trailhawk'],
#         'Nissan': ['350Z', 'Maxima', 'Navara', 'Pulsar'],
#     }
#     ... ? __ ?