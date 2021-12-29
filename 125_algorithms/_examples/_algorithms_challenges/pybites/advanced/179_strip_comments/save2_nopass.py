import re

def strip_comments(code):
    if code.strip().startswith('class'):
        new_code = re.sub(r'#\s.*\n\s*|"{3}[\s\S]*?"{3}\n\s*', '', code)
        output = []
        for line in new_code.splitlines():
            if line.startswith('class'):
                output.append(line)
                output.append('\n')
            else:
                output.append(line)
        return '\n'.join(output)
    return re.sub(r'#\s.*\n\s*|"{3}[\s\S]*?"{3}\n\s*', '', code)