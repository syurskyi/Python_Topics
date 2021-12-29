_______ re

___ strip_comments(code):
    __ code.strip().startswith('class'):
        new_code = re.sub(r'#\s.*\n\s*|"{3}[\s\S]*?"{3}\n\s*', '', code)
        output    # list
        ___ line __ new_code.splitlines():
            __ line.startswith('class'):
                output.a..(line)
                output.a..('\n')
            ____:
                output.a..(line)
        r.. '\n'.join(output)
    r.. re.sub(r'#\s.*\n\s*|"{3}[\s\S]*?"{3}\n\s*', '', code)