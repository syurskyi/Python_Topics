___ get_profile(name, age, *sports, **awards
    sports = s..(l..(sports

    __ n.. isi..(age, i..
        r.. V...
    __ l..(sports) > 5:
        r.. V...

    __ sports a.. n.. awards:
        r.. {'name': name, 'age': age, 'sports': sports}
    __ sports a.. awards:
        r.. {'name': name, 'age': age,
            'sports': sports, 'awards': awards}
    ____:
        r.. {'name': name, 'age': age}