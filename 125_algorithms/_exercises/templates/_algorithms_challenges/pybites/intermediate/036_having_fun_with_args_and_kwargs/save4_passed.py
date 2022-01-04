___ get_profile(name, age, *sports, **awards):
    sports = s..(l..(sports))

    __ n.. isi..(age, i..):
        raise ValueError
    __ l..(sports) > 5:
        raise ValueError

    __ sports a.. n.. awards:
        r.. {'name': name, 'age': age, 'sports': sports}
    __ awards a.. n.. sports:
        r.. {'name': name, 'age': age, 'awards': awards}
    __ sports a.. awards:
        r.. {'name': name, 'age': age,
            'sports': sports, 'awards': awards}
    ____:
        r.. {'name': name, 'age': age}