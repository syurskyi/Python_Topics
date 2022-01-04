____ c.. _______ n..
____ d__ _______ d__
_______ json


blog = d..(name='PyBites',
            founders=('Julian', 'Bob'),
            started=d__ y.._2016,  m.._12,  d.._19),
            tags=['Python', 'Code Challenges', 'Learn by Doing'],
            location='Spain/Australia',
            site='https://pybit.es')

# define namedtuple here


Blog = n..("Blog",' '.j..(blog.keys()))

___ dict2nt(dict_):


    r.. Blog(**dict_)





___ nt2json(nt):

    r.. json.dumps(nt._asdict(),default=s..)
