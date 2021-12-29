____ i.. _______ zip_longest

COL_WIDTH = 20


___ _divide_line(line: s.., col_width: int = COL_WIDTH):
    words = line.s..
    result    # list
    line = words[0]
    ___ word __ words[1:]:
        line2 = line + ' ' + word
        __ l..(line2) > col_width:
            result.a..(line)
            line = word
        ____:
            line = line2
    result.a..(line)
    r.. result


___ text_to_columns(text):
    """Split text (input arg) to columns, the amount of double
       newlines (\n\n) in text determines the amount of columns.
       Return a string with the column output like:
       line1\nline2\nline3\n ... etc ...
       See also the tests for more info."""
    lines = [_divide_line(col) ___ col __ (text.s..('\n\n'))]
    rv = [' '.join(combination) ___ combination __ zip_longest(*lines, fillvalue=' ')]
    r.. '\n'.join(rv)
