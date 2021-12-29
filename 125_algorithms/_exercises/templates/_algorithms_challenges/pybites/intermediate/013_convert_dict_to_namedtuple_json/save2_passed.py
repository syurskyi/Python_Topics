____ collections _______ namedtuple
____ datetime _______ datetime
_______ json

blog = d..(name='PyBites',
            founders=('Julian', 'Bob'),
            started=datetime(year=2016, month=12, day=19),
            tags=['Python', 'Code Challenges', 'Learn by Doing'],
            location='Spain/Australia',
            site='https://pybit.es')


___ dict2nt(dict_):
    r.. namedtuple('nt', dict_.keys())(**dict_)


___ nt2json(nt):
    d = nt._asdict()
    r.. json.dumps(d, default=str)