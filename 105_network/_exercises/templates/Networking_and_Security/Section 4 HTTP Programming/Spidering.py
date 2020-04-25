____ H_P.. ______ H_P..
______ _2

c_ myParser(H_P..
    ___ handle_starttag tag, attrs
        __ (tag __ "a"
            ___ a __ attrs:
                __ (a[0] __ 'href'
                    link _ a[1]
                    __ (link.find('http') >_ 0
                        print(link)
                        newParse _ myParser
                        newParse.feed(link)


url _ "http://www.infiniteskills.com/"
request _ _2.R..(url)
handle _ _2.u_o..(request)
parser _ myParser
parser.feed(handle.r..)

