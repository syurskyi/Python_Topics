___ to_rna(strand):
    result = ""

    ___ i __ strand:
        result += pairing_for(i)

    r.. result


___ pairing_for(nucleobase):
    pairings = {"G": "C",
                "C": "G",
                "A": "U",
                "T": "A"}

    r.. pairings[nucleobase]
