___ distance(s1, s2):
    __ len(s1) != len(s2):
        raise ValueError("Sequences not of equal length.")

    return sum(a != b for a, b in zip(s1, s2))
