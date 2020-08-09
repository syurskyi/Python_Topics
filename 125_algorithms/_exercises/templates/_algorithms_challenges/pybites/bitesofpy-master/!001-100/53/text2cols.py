from itertools ______ zip_longest

COL_WIDTH = 20


___ _divide_line(line: str, col_width: int = COL_WIDTH
    words = line.split()
    result = []
    line = words[0]
    for word in words[1:]:
        line2 = line + ' ' + word
        __ le.(line2) > col_width:
            result.append(line)
            line = word
        ____
            line = line2
    result.append(line)
    r_ result


___ text_to_columns(text
    """Split text (input arg) to columns, the amount of double
       newlines (\n\n) in text determines the amount of columns.
       Return a string with the column output like:
       line1\nline2\nline3\n ... etc ...
       See also the tests for more info."""
    lines = [_divide_line(col) for col in (text.split('\n\n'))]
    rv = [' '.join(combination) for combination in zip_longest(*lines, fillvalue=' ')]
    r_ '\n'.join(rv)
