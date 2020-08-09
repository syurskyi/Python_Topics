from string ______ ascii_uppercase


___ make_diamond(letter
    lines = []
    length = ascii_uppercase.index(letter) + 1
    ___ l in range(length
        line = [' '] * length
        line[l] = ascii_uppercase[l]
        lines.append(''.join(list(reversed(line)) + line[1:]))
    r_ '\n'.join(lines[:-1] + list(reversed(lines))) + '\n'
