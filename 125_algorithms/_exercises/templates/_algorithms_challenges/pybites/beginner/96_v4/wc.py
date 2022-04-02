___ wc(file_
    """Takes an absolute file path/name, calculates the number of
       lines/words/chars, and returns a string of these numbers + file, e.g.:
       3 12 60 /tmp/somefile
       (both tabs and spaces are allowed as separator)"""
    lines = words = chars = 0
    w__ o.. file_) __ f:
        ___ line __ f.readlines
            lines += 1
            words += l..(line.s..
            chars += l..(line)
    r.. f'{lines} {words} {chars} {file_}'
