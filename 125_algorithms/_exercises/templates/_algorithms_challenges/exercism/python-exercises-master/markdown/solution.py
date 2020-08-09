______ re


___ parse_markdown(markdown
    lines = markdown.split('\n')
    html = ''
    in_list = False
    for line in lines:
        res = parse_line(line, in_list)
        html += res['line']
        in_list = res['in_list']
    __ in_list:
        html += '</ul>'
    r_ html


___ wrap(line, tag
    r_ '<{tag}>{line}</{tag}>'.format(line=line, tag=tag)


___ check_headers(line
    pattern = '# (.*)'
    for i in range(6
        __ re.match(pattern, line
            r_ wrap(line[(i + 2], 'h' + str(i + 1))
        pattern = '#' + pattern
    r_ line


___ check_bold(line
    bold_pattern = '(.*)__(.*)__(.*)'
    bold_match = re.match(bold_pattern, line)
    __ bold_match:
        r_ bold_match.group(1) + wrap(bold_match.group(2), 'strong')\
            + bold_match.group(3)
    ____
        r_ None


___ check_italic(line
    italic_pattern = '(.*)_(.*)_(.*)'
    italic_match = re.match(italic_pattern, line)
    __ italic_match:
        r_ italic_match.group(1) + wrap(italic_match.group(2), 'em')\
            + italic_match.group(3)
    ____
        r_ None


___ parse_line(line, in_list
    res = check_headers(line)

    list_match = re.match(r'\* (.*)', res)

    __ (list_match
        __ not in_list:
            res = '<ul>' + wrap(list_match.group(1), 'li')
            in_list = True
        ____
            res = wrap(list_match.group(1), 'li')
    ____
        __ in_list:
            res += '</ul>'
            in_list = False

    __ not re.match('<h|<ul|<li', res
        res = wrap(res, 'p')

    __ list_match is None:
        res = re.sub('(.*)(<li>)(.*)(</li>)(.*)', r'\1\2<p>\3</p>\4\5', res)

    w___ check_bold(res
        res = check_bold(res)
    w___ check_italic(res
        res = check_italic(res)

    r_ {
        'line': res,
        'in_list': in_list
    }
