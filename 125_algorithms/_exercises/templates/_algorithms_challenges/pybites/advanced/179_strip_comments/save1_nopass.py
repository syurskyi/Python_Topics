import re

___ strip_comments(code):
    __ code.strip().startswith('class'):
        new_code = re.sub(r'#\s.*\n\s*|"{3}[\s\S]*?"{3}\n\s*', '', code)
        output = []
        for line in new_code.splitlines():
            __ line.startswith('class'):
                output.append(line)
                output.append(' ')
            else:
                output.append(line)
        return '\n'.join(output)
    return re.sub(r'#\s.*\n\s*|"{3}[\s\S]*?"{3}\n\s*', '', code)