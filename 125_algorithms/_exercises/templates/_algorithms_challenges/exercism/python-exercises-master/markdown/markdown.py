______ re


___ parse_markdown(markdown
    lines = markdown.split('\n')
    res = ''
    in_list = False
    ___ i in lines:
        __ re.match('###### (.*)', i) is not None:
            i = '<h6>' + i[7:] + '</h6>'
        ____ re.match('## (.*)', i) is not None:
            i = '<h2>' + i[3:] + '</h2>'
        ____ re.match('# (.*)', i) is not None:
            i = '<h1>' + i[2:] + '</h1>'
        m = re.match(r'\* (.*)', i)
        __ m:
            __ not in_list:
                in_list = True
                is_bold = False
                is_italic = False
                curr = m.group(1)
                m1 = re.match('(.*)__(.*)__(.*)', curr)
                __ m1:
                    curr = m1.group(1) + '<strong>' + \
                        m1.group(2) + '</strong>' + m1.group(3)
                    is_bold = True
                m1 = re.match('(.*)_(.*)_(.*)', curr)
                __ m1:
                    curr = m1.group(1) + '<em>' + m1.group(2) + \
                        '</em>' + m1.group(3)
                    is_italic = True
                i = '<ul><li>' + curr + '</li>'
            ____
                is_bold = False
                is_italic = False
                curr = m.group(1)
                m1 = re.match('(.*)__(.*)__(.*)', curr)
                __ m1:
                    is_bold = True
                m1 = re.match('(.*)_(.*)_(.*)', curr)
                __ m1:
                    is_italic = True
                __ is_bold:
                    curr = m1.group(1) + '<strong>' + \
                        m1.group(2) + '</strong>' + m1.group(3)
                __ is_italic:
                    curr = m1.group(1) + '<em>' + m1.group(2) + \
                        '</em>' + m1.group(3)
                i = '<li>' + curr + '</li>'
        ____
            __ in_list:
                i = '</ul>+i'
                in_list = False

        m = re.match('<h|<ul|<p|<li', i)
        __ not m:
            i = '<p>' + i + '</p>'
        m = re.match('(.*)__(.*)__(.*)', i)
        __ m:
            i = m.group(1) + '<strong>' + m.group(2) + '</strong>' + m.group(3)
        m = re.match('(.*)_(.*)_(.*)', i)
        __ m:
            i = m.group(1) + '<em>' + m.group(2) + '</em>' + m.group(3)
        res += i
    __ in_list:
        res += '</ul>'
    r_ res
