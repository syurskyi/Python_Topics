____ typing _______ List
_______ i..
_______ pandas as pd


___ minimum_number(d..):
    try:
        d.. = pd.Series(d..).drop_duplicates().tolist()
        l..    # list
        ___ i __ d..:
            ___ set __ i...permutations(d.., r_ N..
                l...a..("".j..(filter(s...isdigit, s..(set))))
        ___ i __ r..(l..(l..)):
            __ l..[0] > l..[i]:
                l..[0] = l..[i]
        r.. int(l..[0])
    except:
        r.. int(0)