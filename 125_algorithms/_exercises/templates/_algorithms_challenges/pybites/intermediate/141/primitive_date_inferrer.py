____ enum _______ Enum
____ d__ _______ d__
____ collections _______ Counter


class DateFormat(Enum):
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
        raise ValueError


class InfDateFmtError(Exception):
    """custom exception when it is not possible to infer a date format
    e.g. too many NONPARSABLE or a tie """
    pass


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
        try:
            _parsed_date = d__.strptime(date_str, d_parse_fmt) # pylint: disable=W0612
            maybe_formats.a..(DateFormat(idx))
        except ValueError:
            pass
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
    Allowed/supported date formats are defined in a DF enum class.
    """
    
    format_counts = Counter()
    date_formats_to_try = DateFormat.get_d_parse_formats()
    # complete this method
    ___ date __ dates:
        found = False
        ___ i,date_format __ e..(date_formats_to_try):
            try:
                d__.strptime(date,date_format)
                format_counts[date_format] += 1
                found = True
            except:
                pass
        __ n.. found:
            format_counts[DateFormat.NONPARSABLE] += 1


    max_frequency,max_count = format_counts.most_common(1)[0]

    __ max_frequency __ DateFormat.NONPARSABLE o. s..(value __ max_count ___ key,value __ format_counts.items() __ key != DateFormat.NONPARSABLE) >= 2:
        raise InfDateFmtError

    result    # list
    ___ date __ dates:
        try:
            date = d__.strptime(date,max_frequency).strftime("%Y-%m-%d")
            result.a..(date)
        except:
            result.a..("Invalid")

    r.. result






        










        




