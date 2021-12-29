___ to_rna(strand):
    result = ""

    for i in strand:
        result += pairing_for(i)

    return result


___ pairing_for(nucleobase):
    pairings = {"G": "C",
                "C": "G",
                "A": "U",
                "T": "A"}

    return pairings[nucleobase]
