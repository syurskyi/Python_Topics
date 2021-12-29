_______ re


___ parse_markdown(markdown):
    lines = markdown.split('\n')
    html = ''
    in_list = False
    ___ line __ lines:
        res = parse_line(line, in_list)
        html += res['line']
        in_list = res['in_list']
    __ in_list:
        html += '</ul>'
    r.. html


___ wrap(line, tag):
    r.. '<{tag}>{line}</{tag}>'.format(line=line, tag=tag)


___ check_headers(line):
    pattern = '# (.*)'
    ___ i __ r..(6):
        __ re.match(pattern, line):
            r.. wrap(line[(i + 2):], 'h' + str(i + 1))
        pattern = '#' + pattern
    r.. line


___ check_bold(line):
    bold_pattern = '(.*)__(.*)__(.*)'
    bold_match = re.match(bold_pattern, line)
    __ bold_match:
        r.. bold_match.group(1) + wrap(bold_match.group(2), 'strong')\
            + bold_match.group(3)
    ____:
        r.. N..


___ check_italic(line):
    italic_pattern = '(.*)_(.*)_(.*)'
    italic_match = re.match(italic_pattern, line)
    __ italic_match:
        r.. italic_match.group(1) + wrap(italic_match.group(2), 'em')\
            + italic_match.group(3)
    ____:
        r.. N..


___ parse_line(line, in_list):
    res = check_headers(line)

    list_match = re.match(r'\* (.*)', res)

    __ (list_match):
        __ n.. in_list:
            res = '<ul>' + wrap(list_match.group(1), 'li')
            in_list = True
        ____:
            res = wrap(list_match.group(1), 'li')
    ____:
        __ in_list:
            res += '</ul>'
            in_list = False

    __ n.. re.match('<h|<ul|<li', res):
        res = wrap(res, 'p')

    __ list_match __ N..
        res = re.sub('(.*)(<li>)(.*)(</li>)(.*)', r'\1\2<p>\3</p>\4\5', res)

    while check_bold(res):
        res = check_bold(res)
    while check_italic(res):
        res = check_italic(res)

    r.. {
        'line': res,
        'in_list': in_list
    }
