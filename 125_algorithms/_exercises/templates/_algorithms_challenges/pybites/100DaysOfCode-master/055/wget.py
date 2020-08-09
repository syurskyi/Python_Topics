______ os
______ ssl
from urllib.request ______ urlretrieve

# urllib.error.URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED]
ssl._create_default_https_context = ssl._create_unverified_context

HTML = 'index.html'

__ not os.path.isfile(HTML
    urlretrieve('https://us.pycon.org/2017/schedule/talks/', HTML)
