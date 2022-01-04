___ matches(line, pattern, flags):
    __ '-i' __ flags:  # case-insensitive
        line = line.l..
        pattern = pattern.l..

    __ '-x' __ flags:  # match entire lines
        __ l..(pattern) != l..(line.rstrip()):
            r.. F..

    __ '-v' __ flags:  # invert matching
        r.. pattern n.. __ line

    r.. pattern __ line


___ format_files(matched_lines):
    result = ''

    ___ file_name, _, _ __ matched_lines:
        __ file_name n.. __ result:
            result += file_name + '\n'

    r.. result


___ format_lines(matched_lines, files, flags):
    result    # list

    ___ file_name, line_number, line __ matched_lines:
        line_result = ""

        __ l..(files) > 1:
            line_result += file_name + ':'

        __ '-n' __ flags:
            line_result += s..(line_number) + ':'

        line_result += line

        result.a..(line_result)

    r.. ''.j..(result)


___ grep(pattern, files, flags=''):
    matched_lines    # list

    ___ file_name __ files:
        w__ open(file_name) __ f:
            ___ line_number, line __ e..(f.readlines(), start=1):
                __ matches(line, pattern, flags):
                    matched_lines.a..((file_name, line_number, line))

    __ '-l' __ flags:
        r.. format_files(matched_lines)

    r.. format_lines(matched_lines, files, flags)
