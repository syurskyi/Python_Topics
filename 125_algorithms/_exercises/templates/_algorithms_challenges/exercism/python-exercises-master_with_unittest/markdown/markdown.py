_______ __


___ parse_markdown(markdown):
    lines = markdown.s..('\n')
    res = ''
    in_list = F..
    ___ i __ lines:
        __ __.match('###### (.*)', i) __ n.. N..
            i = '<h6>' + i[7:] + '</h6>'
        ____ __.match('## (.*)', i) __ n.. N..
            i = '<h2>' + i[3:] + '</h2>'
        ____ __.match('# (.*)', i) __ n.. N..
            i = '<h1>' + i[2:] + '</h1>'
        m = __.match(r'\* (.*)', i)
        __ m:
            __ n.. in_list:
                in_list = T..
                is_bold = F..
                is_italic = F..
                curr = m.group(1)
                m1 = __.match('(.*)__(.*)__(.*)', curr)
                __ m1:
                    curr = m1.group(1) + '<strong>' + \
                        m1.group(2) + '</strong>' + m1.group(3)
                    is_bold = T..
                m1 = __.match('(.*)_(.*)_(.*)', curr)
                __ m1:
                    curr = m1.group(1) + '<em>' + m1.group(2) + \
                        '</em>' + m1.group(3)
                    is_italic = T..
                i = '<ul><li>' + curr + '</li>'
            ____:
                is_bold = F..
                is_italic = F..
                curr = m.group(1)
                m1 = __.match('(.*)__(.*)__(.*)', curr)
                __ m1:
                    is_bold = T..
                m1 = __.match('(.*)_(.*)_(.*)', curr)
                __ m1:
                    is_italic = T..
                __ is_bold:
                    curr = m1.group(1) + '<strong>' + \
                        m1.group(2) + '</strong>' + m1.group(3)
                __ is_italic:
                    curr = m1.group(1) + '<em>' + m1.group(2) + \
                        '</em>' + m1.group(3)
                i = '<li>' + curr + '</li>'
        ____:
            __ in_list:
                i = '</ul>+i'
                in_list = F..

        m = __.match('<h|<ul|<p|<li', i)
        __ n.. m:
            i = '<p>' + i + '</p>'
        m = __.match('(.*)__(.*)__(.*)', i)
        __ m:
            i = m.group(1) + '<strong>' + m.group(2) + '</strong>' + m.group(3)
        m = __.match('(.*)_(.*)_(.*)', i)
        __ m:
            i = m.group(1) + '<em>' + m.group(2) + '</em>' + m.group(3)
        res += i
    __ in_list:
        res += '</ul>'
    r.. res
