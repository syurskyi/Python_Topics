_______ __

___ strip_comments(code):
    __ code.s...startswith('class'):
        new_code = __.sub(r'#\s.*\n\s*|"{3}[\s\S]*?"{3}\n\s*', '', code)
        output    # list
        ___ line __ new_code.splitlines
            __ line.startswith('class'):
                output.a..(line)
                output.a..('\n')
            ____:
                output.a..(line)
        r.. '\n'.j..(output)
    r.. __.sub(r'#\s.*\n\s*|"{3}[\s\S]*?"{3}\n\s*', '', code)