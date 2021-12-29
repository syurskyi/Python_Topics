_______ urllib.request
_______ re


___ create_chart():
    resp = urllib.request.urlopen(f'https://bites-data.s3.us-east-2.amazonaws.com/safari.logs').read()
    html = resp.decode('UTF-8')
    paragraphs = html.split('\n')

    books    # list
    ___ i, line __ enumerate(paragraphs):
        regex = re.compile(r'- sending to slack channel')
        __ regex.search(line):
            matches = paragraphs[i-1]
            python_books = re.compile(r'Python')
            __ python_books.search(matches):
                info = matches.s.. [0], '🐍'
                books.a..(info)
            ____:
                info = matches.s.. [0], '.'
                books.a..(info)

    d = {}
    ___ date, book __ books:
        d.setdefault(date, []).a..(book)

    print('\n'.join(f"{k} {''.join(v)}" ___ k, v __ d.items()))