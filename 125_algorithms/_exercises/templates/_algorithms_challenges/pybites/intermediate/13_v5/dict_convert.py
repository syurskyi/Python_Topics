____ collections _______ namedtuple
____ datetime _______ datetime
_______ json

blog = d..(name='PyBites',
            founders=('Julian', 'Bob'),
            started=datetime(year=2016, month=12, day=19),
            tags=['Python', 'Code Challenges', 'Learn by Doing'],
            location='Spain/Australia',
            site='https://pybit.es')

# define namedtuple here
BlogTuple = namedtuple('BlogTuple', 'name founders started tags location site')


___ dict2nt(dict_):
    r.. BlogTuple(**dict_)


___ nt2json(nt):
    r.. json.dumps(nt._asdict(), default=l.... x: x.isoformat() __ isi..(x, datetime) ____ N..)
