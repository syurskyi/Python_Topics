___ get_profile(name, age, *sports, **awards):
    __ not isinstance(age, int):
        raise ValueError
    __ len(sports) > 5:
        raise ValueError
    return {'name': name, 'age': age, 
            'sports': list(sports), 'awards': awards}