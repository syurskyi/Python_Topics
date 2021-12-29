___ transpose(input_lines):
    lines = input_lines.s..("\n")
    zipped = map(l..,
                 [line.ljust(l..(max(lines, key=l..)))
                  ___ line __ lines])
    r.. "\n".join("".join(line) ___ line __ z..(*zipped)).s..
