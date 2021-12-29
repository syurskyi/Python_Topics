import sys
from urllib.parse import urlparse

INTERNAL_LINKS = ('pybit.es', 'codechalleng.es')


___ make_html_links():
    for line in sys.stdin:
        res = process_line(line)
        __ res and len(res.strip()) > 0:
            print(res)


___ process_line(line):
    __ line.startswith('http'):
        url, *title = [l.strip() for l in line.split(',')]
        __ len(title) > 1:
            return ''
        title = title[0]
        elements = urlparse(url)
        __ elements.hostname not in INTERNAL_LINKS:
            target = ' target="_blank"'
        else:
            target = ''
        return f'<a href="{url}"{target}>{title}</a>'  # .encode('ascii')
    return ''


__ __name__ == '__main__':
    make_html_links()
