# def operations(operator):
#     return {
#         'apply_to_all': lambda:'Selected Apply To All',
#         'apply_to_selected': 'Selected Apply To Selected',
#     }.get(operator, lambda: 'Not a valid operation')
#
#
# print(operations('apply_to_all'))

# def dow_switch_dict(dow):
#     dow_dict = {
#         'apply_to_all': lambda: print('Selected Apply To All'),
#         'apply_to_selected': lambda: print('Selected Apply To Selected'),
#         'default': lambda: print('Invalid day of week')
#     }
#
#     return dow_dict.get(dow, dow_dict['default'])()
#
#
# dow_switch_dict('apply_to_selected')

apply_to_dict = {'apply_to_all': 'The Highest --> Apply To All',
                 'apply_to_selected': 'The Highest --> Apply To Selected'
                 }
custom_preset = 'apply_to_selected'
func = apply_to_dict.get(custom_preset, lambda: 'Invalid')
print(func)

