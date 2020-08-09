___ get_profile(name: str, age: int, *sports, **awards
    __ not isinstance(age, int
        raise ValueError("Age must be a whole number")
    __ le.(sports) > 5:
        raise ValueError("A maximum of five sports are allowed")
    res = {"name": name, "age": age}
    __ le.(sports) > 0:
        res["sports"] = sorted(sports)
    __ le.(awards) > 0:
        res["awards"] = awards
    r_ res
