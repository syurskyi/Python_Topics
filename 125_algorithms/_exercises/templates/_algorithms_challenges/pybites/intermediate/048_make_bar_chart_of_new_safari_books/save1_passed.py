_______ urllib.request
_______ __


___ create_chart
    resp = urllib.request.urlopen _*https://bites-data.s3.us-east-2.amazonaws.com/safari.logs').read()
    html = resp.d.. 'UTF-8')
    paragraphs = html.s..('\n')

    books    # list
    ___ i, line __ e..(paragraphs
        regex = __.c..(r'- sending to slack channel')
        __ regex.s..(line
            matches = paragraphs[i-1]
            python_books = __.c..(r'Python')
            __ python_books.s..(matches
                info = matches.s.. [0], '🐍'
                books.a..(info)
            ____:
                info = matches.s.. [0], '.'
                books.a..(info)

    d    # dict
    ___ date, book __ books:
        d.setdefault(date, []).a..(book)

    print('\n'.j..(f"{k} {''.j..(v)}" ___ k, v __ d.items()))