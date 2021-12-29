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


Blog = namedtuple("Blog",' '.join(blog.keys()))

___ dict2nt(dict_):


    r.. Blog(**dict_)





___ nt2json(nt):

    r.. json.dumps(nt._asdict(),default=str)
