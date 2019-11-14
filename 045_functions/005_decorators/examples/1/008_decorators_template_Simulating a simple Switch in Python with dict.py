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


dow_switch_dict(1)
dow_switch_dict(100)