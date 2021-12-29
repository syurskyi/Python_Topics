____ datetime _______ date
____ itertools _______ islice

____ notifications _______ gen_bite_planning

TODAY = date(2019, 8, 25)


___ test_one_bite_a_day():
    gen = gen_bite_planning(num_bites=1, num_days=1, start_date=TODAY)
    actual = l..(islice(gen, 10))
    expected = [date(2019, 8, 26), date(2019, 8, 27),
                date(2019, 8, 28), date(2019, 8, 29),
                date(2019, 8, 30), date(2019, 8, 31),
                date(2019, 9, 1), date(2019, 9, 2),
                date(2019, 9, 3), date(2019, 9, 4)]
    ... actual __ expected


___ test_two_bites_every_three_days():
    gen = gen_bite_planning(num_bites=2, num_days=3, start_date=TODAY)
    actual = l..(islice(gen, 10))
    expected = [date(2019, 8, 28), date(2019, 8, 28),
                date(2019, 8, 31), date(2019, 8, 31),
                date(2019, 9, 3), date(2019, 9, 3),
                date(2019, 9, 6), date(2019, 9, 6),
                date(2019, 9, 9), date(2019, 9, 9)]
    ... actual __ expected


___ test_one_bite_every_other_day():
    gen = gen_bite_planning(num_bites=1, num_days=2, start_date=TODAY)
    actual = l..(islice(gen, 10))
    expected = [date(2019, 8, 27), date(2019, 8, 29),
                date(2019, 8, 31), date(2019, 9, 2),
                date(2019, 9, 4), date(2019, 9, 6),
                date(2019, 9, 8), date(2019, 9, 10),
                date(2019, 9, 12), date(2019, 9, 14)]
    ... actual __ expected