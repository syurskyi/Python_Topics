___ get_profile(name, age, *sports, **awards):
    
    __ not isinstance(age, int):
        raise ValueError
    __ len(sports) > 5:
        raise ValueError

    __ sports and not awards:
        return {'name': name, 'age': age, 'sports': list(sports)}
    __ sports and awards:
        return {'name': name, 'age': age,
            'sports': list(sports), 'awards': awards}
    else:
        return {'name': name, 'age': age}