from collections ______ namedtuple
from datetime ______ datetime
______ json

blog = dict(name='PyBites',
            founders=('Julian', 'Bob'),
            started=datetime(year=2016, month=12, day=19),
            tags=['Python', 'Code Challenges', 'Learn by Doing'],
            location='Spain/Australia',
            site='https://pybit.es')

# define namedtuple here
BlogTuple = namedtuple('BlogTuple', 'name founders started tags location site')


___ dict2nt(dict_
    r_ BlogTuple(**dict_)


___ nt2json(nt
    r_ json.dumps(nt._asdict(), default=lambda x: x.isoformat() __ isinstance(x, datetime) else None)
