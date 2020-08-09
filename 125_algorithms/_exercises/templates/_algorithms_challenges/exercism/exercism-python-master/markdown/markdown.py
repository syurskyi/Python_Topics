______ re


___ parse_markdown(markdown
    res = []
    for line in markdown.split('\n'
        line = re.sub(r'__(.*?)__', r'<strong>\1</strong>', line)
        line = re.sub(r'_(.*?)_', r'<em>\1</em>', line)

        header_match = re.match(r'(#+) (.*)', line)
        __ header_match:
            res.append('<h{0}>{1}</h{0}>'.format(
                le.(header_match.group(1)), header_match.group(2)))
        ____ line.startswith('* '
            __ res and res[-1] __ '</ul>':
                res.pop()
            ____
                res.append('<ul>')
            res.append('<li>' + line[2:] + '</li>')
            res.append('</ul>')
        ____
            res.append('<p>' + line + '</p>')
    r_ ''.join(res)
