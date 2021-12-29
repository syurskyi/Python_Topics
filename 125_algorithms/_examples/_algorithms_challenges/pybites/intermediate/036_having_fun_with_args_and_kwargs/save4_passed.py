def get_profile(name, age, *sports, **awards):
    sports = sorted(list(sports))

    if not isinstance(age, int):
        raise ValueError
    if len(sports) > 5:
        raise ValueError

    if sports and not awards:
        return {'name': name, 'age': age, 'sports': sports}
    if awards and not sports:
        return {'name': name, 'age': age, 'awards': awards}
    if sports and awards:
        return {'name': name, 'age': age,
            'sports': sports, 'awards': awards}
    else:
        return {'name': name, 'age': age}