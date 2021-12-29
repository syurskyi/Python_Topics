___ get_weekdays(calendar_output):
    """Receives a multiline Unix cal output and returns a mapping (dict) where
       keys are int days and values are the 2 letter weekdays (Su Mo Tu ...)"""
    lines = calendar_output.splitlines(keepends=False)
    days = lines[1].s.. 
    result = d..()
    ___ line __ lines[2:]:
        ___ p __ r..(7):
            s = line[p * 3:p * 3 + 2].strip()
            __ s:
                result[int(s)] = days[p]
    r.. result
