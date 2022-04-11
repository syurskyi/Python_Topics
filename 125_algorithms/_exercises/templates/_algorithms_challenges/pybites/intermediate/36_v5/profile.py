___ get_profile(name: s.., age: i.., *sports, **awards
    __ n.. isi..(age, i..
        r.. V...("Age must be a whole number")
    __ l..(sports) > 5:
        r.. V...("A maximum of five sports are allowed")
    res {"name": name, "age": age}
    __ l..(sports) > 0:
        res["sports"] s..(sports)
    __ l..(awards) > 0:
        res["awards"] awards
    r.. res
