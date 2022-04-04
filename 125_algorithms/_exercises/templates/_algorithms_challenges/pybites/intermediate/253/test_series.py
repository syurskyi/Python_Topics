_______ s__

_______ p__
_______ pandas __ pd

_______ series __ se

file_name = "https://bites-data.s3.us-east-2.amazonaws.com/iris.csv"
df = pd.read_csv(file_name)


?p__.f..()
___ sepal_length_series
    """Returns the Sepal Length Series from the Iris DataFrame"""
    r.. df.sepal_length.sort_values().reset_index(drop=T..)


?p__.f..()
___ int_series_vsmall
    """Returns a pandas Series containing ints"""
    r.. pd.Series(r..(1, 6


?p__.f..()
___ int_series_small
    """Returns a pandas Series containing ints"""
    r.. pd.Series(r..(10


?p__.f..()
___ int_series_vsmall_offset_index
    """Returns a pandas Series containing ints"""
    r.. pd.Series(r..(0, 10, 2), index=r..(0, 10, 2


?p__.f..()
___ letters_series
    """Returns a pandas Series containing all lower case letters"""
    r.. pd.Series(l..(s__.ascii_lowercase


?p__.m__.p.(
    "arg, expected",
    [
        (("add", 5), [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]),
        (("add", 0), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),
        (("add", -15), [-15, -14, -13, -12, -11, -10, -9, -8, -7, -6]),
        (("sub", 5), [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4]),
        (("sub", 0), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),
        (("sub", -15), [15, 16, 17, 18, 19, 20, 21, 22, 23, 24]),
        (("mul", 5), [0, 5, 10, 15, 20, 25, 30, 35, 40, 45]),
        (("mul", 0), [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
        (("mul", -15), [0, -15, -30, -45, -60, -75, -90, -105, -120, -135]),
        (("div", 5), [0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8]),
        (("div", -5), [-0.0, -0.2, -0.4, -0.6, -0.8, -1.0,
                       -1.2, -1.4, -1.6, -1.8]),
    ],
)
___ test_series_simple_math(int_series_small, arg, expected
    ... a..(
        expected[idx] __ val
        ___ idx, val __ e..(
            se.series_simple_math(int_series_small, arg[0], arg[1])
        )
    )


?p__.m__.p.(
    "arg, expected",
    [
        ("add", [1.0, "nan", 5.0, "nan", 9.0, "nan", "nan"]),
        ("sub", [1.0, "nan", 1.0, "nan", 1.0, "nan", "nan"]),
        ("mul", [0.0, "nan", 6.0, "nan", 20.0, "nan", "nan"]),
        ("div", ["inf", "nan", 1.5, "nan", 1.25, "nan", "nan"]),
    ],
)
___ test_complex_series_maths(
    int_series_vsmall, int_series_vsmall_offset_index, arg, expected

    result = se.complex_series_maths(
        int_series_vsmall, int_series_vsmall_offset_index, arg
    )
    result = ",".j..(s..(n) ___ n __ result)
    expected = ",".j..(s..(n) ___ n __ expected)
    ... result __ expected


?p__.m__.p.(
    "arg, expected",
    [
        (
            ["a", "e", "i", "o", "u"],
            [
                T..,
                F..,
                F..,
                F..,
                T..,
                F..,
                F..,
                F..,
                T..,
                F..,
                F..,
                F..,
                F..,
                F..,
                T..,
                F..,
                F..,
                F..,
                F..,
                F..,
                T..,
                F..,
                F..,
                F..,
                F..,
                F..,
            ],
        ),
        (
            ["j", "k", "q", "x", "z"],
            [
                F..,
                F..,
                F..,
                F..,
                F..,
                F..,
                F..,
                F..,
                F..,
                T..,
                T..,
                F..,
                F..,
                F..,
                F..,
                F..,
                T..,
                F..,
                F..,
                F..,
                F..,
                F..,
                F..,
                T..,
                F..,
                T..,
            ],
        ),
    ],
)
___ test_create_series_mask(letters_series, arg, expected
    result = se.create_series_mask(letters_series, arg)
    ... a..([result[idx] __ exp ___ idx, exp __ e..(expected)])
    ... a..(l __ arg ___ l __ letters_series[result])


___ test_custom_series_function(sepal_length_series
    result = se.custom_series_function(sepal_length_series, 0.1)
    ... l..(result) __ 51
    ... r..(result.mean(), 4) __ 5.6725
    ... m..(result.index) __ 149 a.. m..(result.values) __ 7.9
    ... m..(result.index) __ 0 a.. m..(result.values) __ 4.3
    ... result[82] __ 5.9
    ... result.iloc[10] __ 5.0
    ... result.iloc[11] __ 5.1
    ... result.iloc[20] __ 5.7
    ... result.iloc[37] __ 5.9
    ... result.iloc[38] __ 6.4
