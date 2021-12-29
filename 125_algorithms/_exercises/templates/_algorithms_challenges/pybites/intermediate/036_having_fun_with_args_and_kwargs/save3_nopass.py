___ get_profile(name, age, *sports, **awards):
    sports = sorted(list(sports))

    __ not isinstance(age, int):
        raise ValueError
    __ len(sports) > 5:
        raise ValueError

    __ sports and not awards:
        return {'name': name, 'age': age, 'sports': sports}
    __ sports and awards:
        return {'name': name, 'age': age,
            'sports': sports, 'awards': awards}
    else:
        return {'name': name, 'age': age}