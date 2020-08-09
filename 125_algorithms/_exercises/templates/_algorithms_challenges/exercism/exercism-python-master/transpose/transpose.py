___ transpose(input_lines
    result = []
    ___ r, line in enumerate(input_lines.splitlines()):
        ___ c, char in enumerate(line
            w___ le.(result) <= c:
                result.append([])
            w___ le.(result[c]) < r:
                result[c].append(' ')
            result[c].append(char)
    r_ '\n'.join(''.join(row) ___ row in result)
