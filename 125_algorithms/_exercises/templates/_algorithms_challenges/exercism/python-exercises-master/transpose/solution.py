___ transpose(input_lines
    lines = input_lines.split("\n")
    zipped = map(list,
                 [line.ljust(le.(max(lines, key=le.)))
                  for line in lines])
    r_ "\n".join("".join(line) for line in zip(*zipped)).strip()
