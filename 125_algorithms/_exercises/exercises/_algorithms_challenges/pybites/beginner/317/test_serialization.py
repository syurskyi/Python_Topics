____ d__ _______ d__
_______ t__
____ t___ _______ N..

____ serialization _______ (download_pickle_file,
                           deserialize,
                           serialize,
                           TMP,
                           MovieRented)


c_ Bite(N..
    title: s..
    number: i..
    level: s..


___ test_deserialize_movie_rented_data
    download_pickle_file()
    e.. [
        ? 'Mad Max Fury Road', 4, date(2020, 12, 1,
        ? 'Mad Max Fury Road', 4, date(2020, 12, 17,
        ? 'Die Hard', 4, date(2020, 12, 3,
        ? 'Tenet', 20, date(2020, 12, 1,
        ? 'Breach', 7, date(2020, 11, 17,
        ? 'Spider-Man', 12, date(2020, 12, 28,
        ? 'Sonic', 10, date(2020, 11, 4
    ]
    a.. deserialize()
    ... a.. __ e..


___ test_serialize_and_deserialize_other_data
    data [
        Bite('Sum of Numbers', 1, 'Beginner'),
        Bite('Regex Fun', 2, 'Advanced'),
    ]
    pkl_file TMP / s..(i..(t__.t__()))
    serialize(pkl_file, data=data)
    a.. deserialize(pkl_file)
    e.. data
    ... a.. __ e..