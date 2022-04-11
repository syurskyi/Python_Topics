_______ ___
____ urllib.p.. _______ urlparse

INTERNAL_LINKS ('pybit.es', 'codechalleng.es')


___ make_html_links
    ___ line __ ___.stdin:
        res process_line(line)
        __ res a.. l..(res.s.. > 0:
            print(res)


___ process_line(line
    __ line.s.. 'http'
        url, *title [l.s.. ___ l __ line.s..(',')]
        __ l..(title) > 1:
            r.. ''
        title title[0]
        elements urlparse(url)
        __ elements.hostname n.. __ INTERNAL_LINKS:
            target ' target="_blank"'
        ____
            target ''
        r.. f'<a href="{url}"{target}>{title}</a>'  # .encode('ascii')
    r.. ''


__ _____ __ _____
    make_html_links()
