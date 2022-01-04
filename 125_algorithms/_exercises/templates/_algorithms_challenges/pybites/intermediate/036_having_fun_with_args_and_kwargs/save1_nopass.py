___ get_profile(name, age, *sports, **awards):
    __ n.. isi..(age, i..):
        r.. ValueError
    __ l..(sports) > 5:
        r.. ValueError
    r.. {'name': name, 'age': age,
            'sports': l..(sports), 'awards': awards}