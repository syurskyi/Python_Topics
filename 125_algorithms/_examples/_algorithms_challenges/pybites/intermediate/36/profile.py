def get_profile(name, age, *args, **kwargs):
    return_dict = {}
    if args:
        return_dict['sports'] = sorted(list(args))
    if (isinstance(age, int)) and len(args) <= 5:
        return_dict['name'] = name
        return_dict['age'] = age
        if args:
            return_dict['sports'] = sorted(list(args))
        if kwargs:
            return_dict['awards'] = kwargs
        return return_dict
    else:
        raise ValueError


#print(get_profile('tim', 36, 'tennis', 'basketball', 'archery', 'soccer', 'badminton', champ='helped out team in crisis', winner='python') )
print(get_profile('tim', 36, 'tennis') )