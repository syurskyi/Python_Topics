_______ re


___ password_complexity(password: str):
    """Input: password string, calculate score according to 5 criteria in bite,
       return: score int"""
    up = lo = num = spec = 0
    ___ l __ password:
        __ l.isupper():
            up += 1
        ____ l.islower():
            lo += 1
        ____ l.isdigit():
            num += 1
        ____:
            spec += 1
    score = 0
    __ 0 < up and 0 < lo:
        score += 1
    __ 0 < up + lo and 0 < num:
        score += 1
    __ 0 < spec:
        score += 1
    __ l..(password) >= 8:
        score += 1
        __ n.. re.search(r'(.)\1', password):
            score += 1
    r.. score
