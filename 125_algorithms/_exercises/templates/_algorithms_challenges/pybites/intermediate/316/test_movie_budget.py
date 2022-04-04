____ d__ _______ date

_______ p__

____ movie_budget _______ rent_or_stream, MovieRented


?p__.m__.p.("arg, expected", [
   ([MovieRented('Mad Max Fury Road', 4, date(2020, 12, 1],
    {"2020-12": "rent"}),
   ([MovieRented('Mad Max Fury Road', 4, date(2020, 12, 17,
     MovieRented('Die Hard', 4, date(2020, 12, 3,
     MovieRented('Wonder Woman', 4, date(2020, 12, 28],
    {"2020-12": "rent"}),
   ([MovieRented('Tenet', 20, date(2020, 12, 1],
    {"2020-12": "stream"}),
   ([MovieRented('Breach', 7, date(2020, 11, 17,
     MovieRented('Die Hard', 4, date(2020, 11, 3,
     MovieRented('Tenet', 20, date(2020, 12, 28],
    {"2020-11": "rent", "2020-12": 'stream'}),
   ([MovieRented('Spider-Man', 12, date(2020, 12, 28,
     MovieRented('Sonic', 10, date(2020, 11, 4,
     MovieRented('Die Hard', 3, date(2020, 11, 3],
    {"2020-11": "stream", "2020-12": 'rent'}),
])
___ test_rent_or_stream(arg, expected
    ... rent_or_stream(arg) __ expected