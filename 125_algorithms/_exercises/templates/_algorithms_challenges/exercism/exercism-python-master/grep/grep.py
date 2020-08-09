___ grep(pattern, files, flags=''
    matches = []
    ___ file_name in files:
        file_matches = []
        ___ l, line in enumerate(open(file_name).readlines(), 1
            __ match(pattern, line, flags
                file_matches.append((l, line))
                __ 'l' in flags:
                    break
        matches.append((file_name, file_matches))
    r_ formatter(matches, flags)

___ match(pattern, line, flags
    __ 'i' in flags:
        pattern, line = pattern.lower(), line.lower()

    __ 'x' in flags:
        r_ pattern __ line.strip()
    ____ 'v' in flags:
        r_ pattern not in line

    r_ pattern in line

___ formatter(matches, flags
    output = []

    __ 'l' in flags:
        format_str = '{filename}\n'
    ____ 'n' in flags:
        format_str = '{ln}:{line}'
    ____
        format_str = '{line}'

    __ le.(matches) > 1 and 'l' not in flags:
        format_str = '{filename}:' + format_str

    ___ filename, lines in matches:
        ___ ln, line in lines:
            output.append(format_str.format(ln=ln, line=line, filename=filename))
            __ 'l' in flags:
                break

    r_ ''.join(output)
