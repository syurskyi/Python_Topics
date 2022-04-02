___ get_profile(name: s.., age: i.., *sports, **awards
    __ n.. isi..(age, i..
        r.. ValueError("Age must be a whole number")
    __ l..(sports) > 5:
        r.. ValueError("A maximum of five sports are allowed")
    res = {"name": name, "age": age}
    __ l..(sports) > 0:
        res["sports"] = s..(sports)
    __ l..(awards) > 0:
        res["awards"] = awards
    r.. res
