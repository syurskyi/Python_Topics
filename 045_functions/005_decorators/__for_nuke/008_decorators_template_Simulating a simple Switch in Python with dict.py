def dow_switch_dict(dow):
    dow_dict = {
        1: lambda: print('Monday'),
        2: lambda: print('Tuesday'),
        3: lambda: print('Wednesday'),
        4: lambda: print('Thursday'),
        5: lambda: print('Friday'),
        6: lambda: print('Saturday'),
        7: lambda: print('Sunday'),
        'default': lambda: print('Invalid day of week')
    }

    return dow_dict.get(dow, dow_dict['default'])()


# dow_switch_dict(1)
# dow_switch_dict(100)


# def dow_switch_test(*dow):
#     dow_dict = {'apply to all': {'error': lambda: print("Error"),
#                                  'black': lambda: print('Black'),
#                                  'checkboard': lambda: print('Checkboard')},
#                 'apply to selected': {'error': lambda: print("Error"),
#                                       'black': lambda :print('Black'),
#                                       'checkboard': lambda: print('Checkboard')}
#                 }
#     return dow_dict.get(dow, dow_dict['default'])
#
#
# dow_switch_test()

people = {1: {'name': 'John', 'age': '27', 'sex':lambda x: x ** 2},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}}
#
print(people[1]['name'])
print(people[1]['age'])
print(people[1]['sex'](3))

# print((lambda x: x + 1)(2))

# # dictionary of functions
# exponent = {'square':lambda x: x ** 2,
#             'cube':lambda x: x ** 3}
#
# print(exponent['square'](3))
# # Prints 9
#
# print(exponent['cube'](3))
# # Prints 27