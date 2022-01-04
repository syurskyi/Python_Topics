___ get_profile(name, age, *sports, **awards):
    __ n.. isi..(age, i..):
        raise ValueError
    __ l..(sports) > 5:
        raise ValueError
    r.. {'name': name, 'age': age,
            'sports': l..(sports), 'awards': awards}