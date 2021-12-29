____ typing _______ List
_______ i..
_______ pandas as pd


___ minimum_number(digits):
    try:
        digits = pd.Series(digits).drop_duplicates().tolist()
        l..    # list
        ___ i __ digits:
            ___ set __ i...permutations(digits, r_ N..
                l...a..("".join(filter(s...isdigit, s..(set))))
        ___ i __ r..(l..(l..)):
            __ l..[0] > l..[i]:
                l..[0] = l..[i]
        r.. l..[0]
    except:
        r.. 0