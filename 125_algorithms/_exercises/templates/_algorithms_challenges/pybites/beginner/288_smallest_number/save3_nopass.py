____ typing _______ List
_______ i..
_______ pandas as pd


___ minimum_number(digits: List[int]) -> int:
    try:
        digits = pd.Series(digits).drop_duplicates().tolist()
        l..    # list
        ___ i __ digits:
            ___ set __ i...permutations(digits, r_ N..
                l...a..("".join(filter(s...isdigit, s..(set))))
        ___ i __ r..(l..(l..)):
            __ l..[0] > l..[i]:
                l..[0] = l..[i]
        r.. s..(l..[0])
    except:
        r.. s..(0)