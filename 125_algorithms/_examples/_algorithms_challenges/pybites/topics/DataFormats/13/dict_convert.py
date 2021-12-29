from collections import namedtuple
from datetime import datetime
import json


blog = dict(name='PyBites',
            founders=('Julian', 'Bob'),
            started=datetime(year=2016, month=12, day=19),
            tags=['Python', 'Code Challenges', 'Learn by Doing'],
            location='Spain/Australia',
            site='https://pybit.es')

# define namedtuple here
NT = namedtuple('NT', ['name', 'founders', 'started', 'tags', 'location', 'site'])

def dict2nt(dict_):
    #nt = NT(dict_['name'],
    #        dict_['founders'],
    #        dict_['started'],
    #        dict_['tags'],
    #        dict_['location'],
    #        dict_['site']
    #)
    #return nt # my solution
    return NT(**dict_) # better solution


def nt2json(nt):
    return json.dumps(nt._asdict(), default=str)

nt = dict2nt(blog)
print(nt.started)
print(type(nt.started))

print(type(nt))
print(json.dumps(nt._asdict(), default=str))