____ e.. _______ E..
____ d__ _______ d__
____ c.. _______ C..


c_ DateFormat(E..
    DDMMYY 0  # dd/mm/yy
    MMDDYY 1  # mm/dd/yy
    YYMMDD 2  # yy/mm/dd
    NONPARSABLE -999

    @classmethod
    ___ get_d_parse_formats(cls, val_ N..
        """ Arg:
        val(int | None) enum member value
        Returns:
        1. for val=None a list of explicit format strings 
            for all supported date formats in this enum
        2. for val=n an explicit format string for a given enum member value
        """
        d_parse_formats ["_d/%m/%y", "%m/_d/%y", "%y/%m/_d"]
        __ val __ N..
            r.. d_parse_formats
        __ 0 <_ val <_ l..(d_parse_formats
            r.. d_parse_formats[val]
        r.. V...


c_ InfDateFmtError(E..
    """custom exception when it is not possible to infer a date format
    e.g. too many NONPARSABLE or a tie """
    p..


___ _maybe_DateFormats(date_str
    """ Args:
    date_str (str) string representing a date in unknown format
    Returns:
    a list of enum members, where each member represents
    a possible date format for the input date_str
    """
    d_parse_formats DateFormat.get_d_parse_formats()
    maybe_formats    # list
    ___ idx, d_parse_fmt __ e..(d_parse_formats
        ___
            _parsed_date d__.s..(date_str, d_parse_fmt) # pylint: disable=W0612
            maybe_formats.a..(DateFormat(idx
        ______ V..
            p..
    __ l..(maybe_formats) __ 0:
        maybe_formats.a..(DateFormat.NONPARSABLE)
    r.. maybe_formats


___ get_dates(dates
    """ Args:
    dates (list) list of date strings
    where each list item represents a date in unknown format
    Returns:
    list of date strings, where each list item represents
    a date in yyyy-mm-dd format. Date format of input date strings is
    inferred based on the most prevalent format in the dates list.
    Allowed/supported date formats are defined in a DF enum class.
    """
    
    format_counts C..()
    date_formats_to_try DateFormat.get_d_parse_formats()
    # complete this method
    ___ date __ dates:
        found F..
        ___ i,date_format __ e..(date_formats_to_try
            ___
                d__.s..(date,date_format)
                format_counts[date_format] += 1
                found T..
            ______:
                p..
        __ n.. found:
            format_counts[DateFormat.NONPARSABLE] += 1


    max_frequency,max_count format_counts.most_common(1 0

    __ max_frequency __ DateFormat.NONPARSABLE o. s..(value __ max_count ___ key,value __ format_counts.i.. __ key !_ DateFormat.NONPARSABLE) >_ 2:
        r.. InfDateFmtError

    result    # list
    ___ date __ dates:
        ___
            date d__.s..(date,max_frequency).s..("_Y-%m-_d")
            result.a..(date)
        ______:
            result.a..("Invalid")

    r.. result






        










        




