______ sys
from urllib.parse ______ urlparse

INTERNAL_LINKS = ('pybit.es', 'codechalleng.es')


___ make_html_links(
    ___ line in sys.stdin:
        res = process_line(line)
        __ res and le.(res.strip()) > 0:
            print(res)


___ process_line(line
    __ line.startswith('http'
        url, *title = [l.strip() ___ l in line.split(',')]
        __ le.(title) > 1:
            r_ ''
        title = title[0]
        elements = urlparse(url)
        __ elements.hostname not in INTERNAL_LINKS:
            target = ' target="_blank"'
        ____
            target = ''
        r_ f'<a href="{url}"{target}>{title}</a>'  # .encode('ascii')
    r_ ''


__ __name__ __ '__main__':
    make_html_links()
