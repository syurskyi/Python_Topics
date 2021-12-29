def get_profile(name, age, *sports, **awards):
    if not isinstance(age, int):
        raise ValueError
    if len(sports) > 5:
        raise ValueError
    return {'name': name, 'age': age, 
            'sports': list(sports), 'awards': awards}