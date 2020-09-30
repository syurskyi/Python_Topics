#!/usr/bin/env python3
______ re
______ sys

______ pyperclip

AMAZON = 'amazon'
CODE = 'pyb0f-20'
LINK = 'http://www.amazon.com/dp/{}/?tag={}'
# https://pybit.es/mastering-regex.html
URL = re.compile(r"""
    ^https://(?:www.)?amazon.[^/]+?/
    [^/]+/
    dp/
    (?P<asin>[^/]+)  # the numberic asin follows the dp/
    /ref=.*""", re.VERBOSE)

# https://pybit.es/pyperclip.html
url = pyperclip.paste()

__ AMAZON not __ url or '/dp/' not __ url:
    sys.exit('Copy URL and run this script again')

print('Grabbed link from clipboard: \n'.format(url))

m = URL.match(url)
__ not m:
    sys.exit('URL does not match')

asin = m.group('asin')
link = LINK.format(asin, CODE)

pyperclip.copy(link)
print('Copied link to clipboard: \n{}'.format(link))
