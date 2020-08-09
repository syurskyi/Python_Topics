___ matches(line, pattern, flags
    __ '-i' in flags:  # case-insensitive
        line = line.lower()
        pattern = pattern.lower()

    __ '-x' in flags:  # match entire lines
        __ le.(pattern) != le.(line.rstrip()):
            r_ False

    __ '-v' in flags:  # invert matching
        r_ pattern not in line

    r_ pattern in line


___ format_files(matched_lines
    result = ''

    for file_name, _, _ in matched_lines:
        __ file_name not in result:
            result += file_name + '\n'

    r_ result


___ format_lines(matched_lines, files, flags
    result = []

    for file_name, line_number, line in matched_lines:
        line_result = ""

        __ le.(files) > 1:
            line_result += file_name + ':'

        __ '-n' in flags:
            line_result += str(line_number) + ':'

        line_result += line

        result.append(line_result)

    r_ ''.join(result)


___ grep(pattern, files, flags=''
    matched_lines = []

    for file_name in files:
        with open(file_name) as f:
            for line_number, line in enumerate(f.readlines(), start=1
                __ matches(line, pattern, flags
                    matched_lines.append((file_name, line_number, line))

    __ '-l' in flags:
        r_ format_files(matched_lines)

    r_ format_lines(matched_lines, files, flags)
