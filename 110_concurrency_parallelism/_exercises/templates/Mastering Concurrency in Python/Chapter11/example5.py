# ch11/example5.py

import ai..
import aiofiles
import a..

______ __
____ t_i_ ______ d_t_ as timer

? ___ download_html(session, url):
    ? w__ session.g..(url, ssl_F..) as res:
        filename _ 'output/%s.html' % __.path.basename(url)

        ? w__ aiofiles.o..(filename, 'wb') as f:
            w__ T..:
                chunk _ await res.content.read(1024)
                __ not chunk:
                    b..
                await f.write(chunk)

        r_ await res.release()

? ___ main(url):
    ? w__ ?.ClientSession() as session:
        await download_html(session, url)

urls _ [
    'http://packtpub.com',
    'http://python.org',
    'http://docs.python.org/3/library/asyncio',
    'http://aiohttp.readthedocs.io',
    'http://google.com'
]

start _ timer()

loop _ ?.get_event_loop()
loop.run_until_complete(
    ?.gather(*(main(url) ___ url __ urls))
)

print('Took %.2f seconds.' % (timer() - start))
