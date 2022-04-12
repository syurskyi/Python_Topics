_______ __


___ parse_markdown(markdown
    lines markdown.s..('\n')
    html ''
    in_list F..
    ___ line __ lines:
        res parse_line(line, in_list)
        html += res 'line' 
        in_list res 'in_list'
    __ in_list:
        html += '</ul>'
    r.. html


___ wrap(line, tag
    r.. '<{tag}>{line}</{tag}>'.f..(line=line, tag=tag)


___ check_headers(line
    pattern '# (.*)'
    ___ i __ r..(6
        __ __.m..(pattern, line
            r.. wrap(line[(i + 2], 'h' + s..(i + 1
        pattern '#' + pattern
    r.. line


___ check_bold(line
    bold_pattern '(.*)__(.*)__(.*)'
    bold_match __.m..(bold_pattern, line)
    __ bold_match:
        r.. bold_match.group(1) + wrap(bold_match.group(2), 'strong')\
            + bold_match.group(3)
    ____
        r.. N..


___ check_italic(line
    italic_pattern '(.*)_(.*)_(.*)'
    italic_match __.m..(italic_pattern, line)
    __ italic_match:
        r.. italic_match.group(1) + wrap(italic_match.group(2), 'em')\
            + italic_match.group(3)
    ____
        r.. N..


___ parse_line(line, in_list
    res check_headers(line)

    list_match __.m.. _ \* (.*)', res)

    __ (list_match
        __ n.. in_list:
            res '<ul>' + wrap(list_match.group(1), 'li')
            in_list T..
        ____
            res wrap(list_match.group(1), 'li')
    ____
        __ in_list:
            res += '</ul>'
            in_list F..

    __ n.. __.m..('<h|<ul|<li', res
        res wrap(res, 'p')

    __ list_match __ N..
        res __.sub('(.*)(<li>)(.*)(</li>)(.*)', r'\1\2<p>\3</p>\4\5', res)

    w.... check_bold(res
        res check_bold(res)
    w.... check_italic(res
        res check_italic(res)

    r.. {
        'line': res,
        'in_list': in_list
    }
