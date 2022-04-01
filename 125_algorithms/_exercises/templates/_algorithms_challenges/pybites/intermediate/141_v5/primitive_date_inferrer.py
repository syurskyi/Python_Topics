____ c.. _______ Counter
____ d__ _______ d__
____ e.. _______ E..


c_ DateFormat(E..):
    DDMMYY = 0  # dd/mm/yy
    MMDDYY = 1  # mm/dd/yy
    YYMMDD = 2  # yy/mm/dd
    NONPARSABLE = -999

    @classmethod
    ___ get_d_parse_formats(cls, val_ N..
        """ Arg:
        val(int | None) enum member value
        Returns:
        1. for val=None a list of explicit format strings 
            for all supported date formats in this enum
        2. for val=n an explicit format string for a given enum member value
        """
        d_parse_formats = ["%d/%m/%y", "%m/%d/%y", "%y/%m/%d"]
        __ val __ N..
            r.. d_parse_formats
        __ 0 <= val <= l..(d_parse_formats):
            r.. d_parse_formats[val]
        r.. ValueError


c_ InfDateFmtError(E..):
    """custom exception when it is not possible to infer a date format
    e.g. too many NONPARSABLE or a tie """
    p..


___ _maybe_DateFormats(date_str):
    """ Args:
    date_str (str) string representing a date in unknown format
    Returns:
    a list of enum members, where each member represents
    a possible date format for the input date_str
    """
    d_parse_formats = DateFormat.get_d_parse_formats()
    maybe_formats    # list
    ___ idx, d_parse_fmt __ e..(d_parse_formats):
        ___
            _parsed_date = d__.strptime(date_str, d_parse_fmt)  # pylint: disable=W0612
            maybe_formats.a..(DateFormat(idx))
        ______ V..
            p..
    __ l..(maybe_formats) __ 0:
        maybe_formats.a..(DateFormat.NONPARSABLE)
    r.. maybe_formats


___ get_dates(dates):
    """ Args:
    dates (list) list of date strings
    where each list item represents a date in unknown format
    Returns:
    list of date strings, where each list item represents
    a date in yyyy-mm-dd format. Date format of input date strings is
    inferred based on the most prevalent format in the dates list.
    Alowed/supported date formats are defined in a DF enum class.
    """
    result    # list
    fmts = Counter(maybe ___ dt __ dates ___ maybe __ _maybe_DateFormats(dt)).most_common(2)
    __ fmts[0][0] __ DateFormat.NONPARSABLE o. fmts[0][1] __ fmts[1][1]:
        r.. InfDateFmtError()
    fmt = DateFormat.get_d_parse_formats(fmts[0][0].value)

    ___ dt __ dates:
        ___
            result.a..(d__.strptime(dt, fmt).s..('%Y-%m-%d'))
        ______ V..
            result.a..('Invalid')

    r.. result
