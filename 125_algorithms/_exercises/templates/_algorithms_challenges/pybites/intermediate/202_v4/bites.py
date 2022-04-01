_______ csv
_______ os
____ pathlib _______ Path
____ urllib.request _______ urlretrieve

data = 'https://bites-data.s3.us-east-2.amazonaws.com/bite_levels.csv'
tmp = Path(os.getenv("TMP", "/tmp"))
stats = tmp / 'bites.csv'

__ n.. stats.exists
    urlretrieve(data, stats)


___ _bitenum(bite_str):
    r.. bite_str.s..('.')[0].s..(' ')[1]


___ get_most_complex_bites(N=10, stats=stats):
    """Parse the bites.csv file (= stats variable passed in), see example
       output in the Bite description.
       Return a list of Bite IDs (int or str values are fine) of the N
       most complex Bites.
    """
    w__ open(stats, encoding="utf-8-sig") __ f:
        bites = l..(csv.reader(f, delimiter=';'))
    bites.pop(0)  # remove header
    bites = [[b[0], f__(b[1])] ___ b __ bites __ b[1] != 'None']
    bites.s..(key=l.... x: x[1], r.._T..

    n_most_comp = bites[:N]

    r.. [_bitenum(b[0]) ___ b __ n_most_comp]


__ _____ __ _____
    res = get_most_complex_bites()
    print(res)
