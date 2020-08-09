______ os
______ pickle
from pprint ______ pprint as pp
______ sys
______ xml.dom.minidom
______ xmltodict

from goodreads ______ client

from authorize ______ authorize

CONSUMER_KEY = os.environ.get('GR_KEY')
CONSUMER_SECRET = os.environ.get('GR_SECRET')
SESSION = 'session' 

try:
    session = pickle.load(open(SESSION, "rb"))
except F..
    session = authorize()

ACCESS_TOKEN = session.access_token
ACCESS_TOKEN_SECRET = session.access_token_secret

gc = client.GoodreadsClient(CONSUMER_KEY, CONSUMER_SECRET)
gc.authenticate(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

resp = session.get("/updates/friends.xml")
#xml_out = xml.dom.minidom.parseString(resp.content)
d = xmltodict.parse(resp.content)
pp(d)
