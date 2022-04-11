_______ csv
____ p.. _______ P..
____ u__.r.. _______ u..

tmp  P..('/tmp')
stats tmp / 'bites.csv'

__ n.. stats.exists
    u..('https://bit.ly/2MQyqXQ', stats)


___ get_most_complex_bites(N=10, stats=stats
    """Parse the bites.csv file (= stats variable passed in), see example
       output in the Bite description.
       Return a list of Bite IDs (int or str values are fine) of the N
       most complex Bites.
    """
    w__ o.. stats, encoding="utf-8-sig") __ s:
        r.. [x[0] ___ x __ s..(
            [[r..(f__(x 'Bite' .s..(' ')[1], f__(x 'Difficulty' )] ___ x __ csv.DictReader(s, delimiter=';')
             __ x 'Difficulty'  != 'None' , key=l.... x: x[1], r.._T..[:N]]


__ _____ __ _____
    res get_most_complex_bites()
    print(res)
