____ enum _______ Enum
____ d__ _______ d__
____ collections _______ Counter, defaultdict


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
    # complete this method
    return_list    # list
    #
    # to find the most prevalent date format
    enum_dict = defaultdict(int)
    ___ date __ dates:
        enum_list = _maybe_DateFormats(date)
        ___ index __ r..(l..(enum_list)):
            __ enum_list[index].value __ -999:
                enum_dict[-999] += 1
            ____:
                enum_dict[enum_list[index].value] += 1
    sorted_enum = s..(enum_dict, key=enum_dict.get, r.._T..
    # convert to the most prevalent date format
    __ enum_dict[sorted_enum[0]] != enum_dict[sorted_enum[1]] a.. sorted_enum[0] != -999:
        date_str = DateFormat.get_d_parse_formats(sorted_enum[0])
        ___ date __ dates:
            enum_list = _maybe_DateFormats(date)
            __ enum_list[0].value __ -999:
                #print('Invalid')
                return_list.a..('Invalid')
            ____:
                try:
                    return_list.a..(s..(d__.strptime(date, date_str).date())                    )
                except ValueError:
                    return_list.a..("Invalid")
                
                #output_date_str = str(datetime.strptime(date, date_str).date())
                #print(f'good {date} {enum_list[0]} {date_str} {output_date_str}')
                #return_list.append(output_date_str)
    ____:
        raise InfDateFmtError 
    r.. return_list


dates1 = [
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

#enum_list = _maybe_DateFormats("13/12/07")
#print(enum_list[0].value)


#print(get_dates(dates1))