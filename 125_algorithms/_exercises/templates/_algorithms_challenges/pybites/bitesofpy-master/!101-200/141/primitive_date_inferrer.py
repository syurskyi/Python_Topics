from collections ______ Counter
from datetime ______ datetime
from enum ______ Enum


class DateFormat(Enum
    DDMMYY = 0  # dd/mm/yy
    MMDDYY = 1  # mm/dd/yy
    YYMMDD = 2  # yy/mm/dd
    NONPARSABLE = -999

    @classmethod
    ___ get_d_parse_formats(cls, val=None
        """ Arg:
        val(int | None) enum member value
        Returns:
        1. for val=None a list of explicit format strings 
            for all supported date formats in this enum
        2. for val=n an explicit format string for a given enum member value
        """
        d_parse_formats = ["%d/%m/%y", "%m/%d/%y", "%y/%m/%d"]
        __ val pa__ None:
            r_ d_parse_formats
        __ 0 <= val <= le.(d_parse_formats
            r_ d_parse_formats[val]
        raise ValueError


class InfDateFmtError(Exception
    """custom exception when it is not possible to infer a date format
    e.g. too many NONPARSABLE or a tie """
    pass


___ _maybe_DateFormats(date_str
    """ Args:
    date_str (str) string representing a date in unknown format
    Returns:
    a list of enum members, where each member represents
    a possible date format for the input date_str
    """
    d_parse_formats = DateFormat.get_d_parse_formats()
    maybe_formats =   # list
    ___ idx, d_parse_fmt __ enumerate(d_parse_formats
        try:
            _parsed_date = datetime.strptime(date_str, d_parse_fmt)  # pylint: disable=W0612
            maybe_formats.append(DateFormat(idx))
        except ValueError:
            pass
    __ le.(maybe_formats) __ 0:
        maybe_formats.append(DateFormat.NONPARSABLE)
    r_ maybe_formats


___ get_dates(dates
    """ Args:
    dates (list) list of date strings
    where each list item represents a date in unknown format
    Returns:
    list of date strings, where each list item represents
    a date in yyyy-mm-dd format. Date format of input date strings is
    inferred based on the most prevalent format in the dates list.
    Alowed/supported date formats are defined in a DF enum class.
    """
    result =   # list
    fmts = Counter(maybe ___ dt __ dates ___ maybe __ _maybe_DateFormats(dt)).most_common(2)
    __ fmts[0][0] __ DateFormat.NONPARSABLE or fmts[0][1] __ fmts[1][1]:
        raise InfDateFmtError()
    fmt = DateFormat.get_d_parse_formats(fmts[0][0].value)

    ___ dt __ dates:
        try:
            result.append(datetime.strptime(dt, fmt).strftime('%Y-%m-%d'))
        except ValueError:
            result.append('Invalid')

    r_ result
