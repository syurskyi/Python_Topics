# ch11/example6.py

______ req..
______ __

____ t_i_ ______ d_t_ as timer

___ download_html(url):
    res _ ?.g..(url)

    filename _ 'output/%s.html' % __.path.basename(url)
    w__ o..(filename, 'w') as f:
        f.write(res.text)

urls _ [
    'http://packtpub.com',
    'http://python.org',
    'http://docs.python.org/3/library/asyncio',
    'http://aiohttp.readthedocs.io',
    'http://google.com'
]

start _ timer()

___ url __ urls:
    download_html(url)

print('Took %.2f seconds.' % (timer() - start))
