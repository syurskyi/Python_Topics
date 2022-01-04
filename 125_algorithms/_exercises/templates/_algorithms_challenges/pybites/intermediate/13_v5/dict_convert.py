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
BlogTuple = n..('BlogTuple', 'name founders started tags location site')


___ dict2nt(dict_):
    r.. BlogTuple(**dict_)


___ nt2json(nt):
    r.. json.dumps(nt._asdict(), default=l.... x: x.isoformat() __ isi..(x, d__) ____ N..)
