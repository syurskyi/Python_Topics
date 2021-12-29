import urllib.request
import re


def create_chart():
    resp = urllib.request.urlopen(f'https://bites-data.s3.us-east-2.amazonaws.com/safari.logs').read()
    html = resp.decode('UTF-8')
    paragraphs = html.split('\n')

    books = []
    for i, line in enumerate(paragraphs):
        regex = re.compile(r'- sending to slack channel')
        if regex.search(line):
            matches = paragraphs[i-1]
            python_books = re.compile(r'Python')
            if python_books.search(matches):
                info = matches.split()[0], '🐍'
                books.append(info)
            else:
                info = matches.split()[0], '.'
                books.append(info)

    d = {}
    for date, book in books:
        d.setdefault(date, []).append(book)

    print('\n'.join(f"{k} {''.join(v)}" for k, v in d.items()))