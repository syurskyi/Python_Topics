_______ p__
____ primitive_date_inferrer _______ get_dates, InfDateFmtError


___ test_tie
    """ any date string can be parsed using the following formats:
    dd/mm/yy , mm/dd/yy, yy/mm/dd
    so no the prevalent format cannot be inferred """
    dates = [
        "11/11/07",
        "01/05/07",
        "05/12/04",
        "06/11/01",
        "10/03/09",
        "10/08/09",
        "04/11/11",
        "02/05/10",
        "05/10/08",
        "12/03/01",
        "10/10/12",
        "03/10/02",
    ]
    w__ p__.r..(InfDateFmtError
        get_dates(dates)


___ test_too_many_nonparsable
    """{<DateFormat.MMDDYY: 1>: 2,  <DateFormat.NONPARSABLE: -999>: 5,
         <DateFormat.DDMMYY: 0>: 2, <DateFormat.YYMMDD: 2>: 3}
    """
    dates = [
        "12/22/68",
        "31/09/87",
        "37/13/29",
        "41/28/13",
        "13/03/32",
        "18/08/74",
        "46/09/27",
        "49/07/10",
        "05/31/88",
        "28/13/17",
        "71/14/19",
        "85/08/09",
    ]
    w__ p__.r..(InfDateFmtError
        get_dates(dates)


___ test_mmddyy
    """ {<DateFormat.MMDDYY: 1>: 7, <DateFormat.DDMMYY: 0>: 5,
         <DateFormat.YYMMDD: 2>: 5, <DateFormat.NONPARSABLE: -999>: 2}
        the single most prevalent format is mm/dd/yy
    """
    dates = [
        "04/25/79",
        "08/09/70",
        "08/04/10",
        "95/31/10",
        "06/13/34",
        "04/03/22",
        "67/12/17",
        "34/10/12",
        "04/05/94",
        "07/12/41",
        "88/11/05",
        "96/26/08",
    ]
    results = [
        "1979-04-25",
        "1970-08-09",
        "2010-08-04",
        "Invalid",
        "2034-06-13",
        "2022-04-03",
        "Invalid",
        "Invalid",
        "1994-04-05",
        "2041-07-12",
        "Invalid",
        "Invalid",
    ]
    ... get_dates(dates) __ results


___ test_yymmdd
    """ {<DateFormat.YYMMDD: 2>: 7, <DateFormat.NONPARSABLE: -999>: 1,
         <DateFormat.MMDDYY: 1>: 3, <DateFormat.DDMMYY: 0>: 3}
         the single most prevalent format is yy/mm/dd """
    dates = [
        "68/12/22",
        "31/09/87",
        "37/03/29",
        "11/28/03",
        "02/03/32",
        "18/08/74",
        "46/09/27",
        "49/07/10",
        "05/31/88",
        "28/12/17",
        "71/04/19",
        "85/08/09",
    ]
    results = [
        "2068-12-22",
        "Invalid",
        "2037-03-29",
        "Invalid",
        "Invalid",
        "Invalid",
        "2046-09-27",
        "2049-07-10",
        "Invalid",
        "2028-12-17",
        "1971-04-19",
        "1985-08-09",
    ]
    ... get_dates(dates) __ results


___ test_ddmmyy
    """ {<DateFormat.MMDDYY: 1>: 7, <DateFormat.DDMMYY: 0>: 9,
        <DateFormat.YYMMDD: 2>: 4}
        the single most prevalent format is dd/mm/yy """
    dates = [
        "12/16/30",
        "16/03/54",
        "97/07/26",
        "04/04/31",
        "01/08/07",
        "02/02/29",
        "73/03/08",
        "06/07/55",
        "10/09/77",
        "18/03/43",
        "30/11/24",
        "08/01/51",
    ]
    results = [
        "Invalid",
        "2054-03-16",
        "Invalid",
        "2031-04-04",
        "2007-08-01",
        "2029-02-02",
        "Invalid",
        "2055-07-06",
        "1977-09-10",
        "2043-03-18",
        "2024-11-30",
        "2051-01-08",
    ]
    ... get_dates(dates) __ results


___ test_different_enum
    """ Modified enum - now it supports 4 different time formats.
        Order of formats is changed as well"""
    ____ e.. _______ E..
    # import the module with the tested code which contains the original emum
    _______ primitive_date_inferrer __ pdi

    c_ DateFormat_ext(E..
        DDMMYYYY = 0
        DDMMYY = 1
        YYMMDD = 2
        MMDDYY = 3
        NONPARSABLE = -999

        @classmethod
        ___ get_d_parse_formats(cls, idx_ N..
            d_parse_formats = ["%d.%m.%Y", "%d/%m/%y", "%y/%m/%d", "%m/%d/%y"]
            __ idx __ N..
                r.. d_parse_formats
            __ 0 <= idx <= l..(d_parse_formats
                r.. d_parse_formats[idx]
            r.. V...

    # override the enum in the tested code module
    pdi.DateFormat = DateFormat_ext

    dates = [
        "12/16/30",
        "16.03.1954",
        "97/07/26",
        "04.04.1931",
        "01.08.1907",
        "02/02/29",
        "73/03/08",
        "06.07.1955",
        "10.09.1977",
        "18.03.1943",
        "30/11/24",
        "08.01.1951",
    ]
    results = [
        "Invalid",
        "1954-03-16",
        "Invalid",
        "1931-04-04",
        "1907-08-01",
        "Invalid",
        "Invalid",
        "1955-07-06",
        "1977-09-10",
        "1943-03-18",
        "Invalid",
        "1951-01-08",
    ]
    ... get_dates(dates) __ results
