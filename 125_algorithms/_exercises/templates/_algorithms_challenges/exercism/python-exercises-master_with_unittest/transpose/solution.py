___ transpose(input_lines):
    lines = input_lines.s..("\n")
    zipped = map(l..,
                 [line.ljust(l..(m..(lines, key=l..)))
                  ___ line __ lines])
    r.. "\n".j..("".j..(line) ___ line __ z..(*zipped)).s..
