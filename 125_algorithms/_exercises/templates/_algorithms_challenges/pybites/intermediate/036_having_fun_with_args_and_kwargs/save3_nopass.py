___ get_profile(name, age, *sports, **awards):
    sports = s..(l..(sports))

    __ n.. isi..(age, int):
        raise ValueError
    __ l..(sports) > 5:
        raise ValueError

    __ sports and n.. awards:
        r.. {'name': name, 'age': age, 'sports': sports}
    __ sports and awards:
        r.. {'name': name, 'age': age,
            'sports': sports, 'awards': awards}
    ____:
        r.. {'name': name, 'age': age}