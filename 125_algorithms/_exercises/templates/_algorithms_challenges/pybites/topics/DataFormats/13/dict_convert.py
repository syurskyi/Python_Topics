____ c.. _______ n..
____ d__ _______ d__
_______ json


blog = d..(name='PyBites',
            founders=('Julian', 'Bob'),
            started=d__ y.._2016,  m.._12,  d.._19),
            tags= 'Python', 'Code Challenges', 'Learn by Doing' ,
            location='Spain/Australia',
            site='https://pybit.es')

# define namedtuple here
NT = n..('NT',  'name', 'founders', 'started', 'tags', 'location', 'site' )

___ dict2nt(dict_
    #nt = NT(dict_['name'],
    #        dict_['founders'],
    #        dict_['started'],
    #        dict_['tags'],
    #        dict_['location'],
    #        dict_['site']
    #)
    #return nt # my solution
    r.. NT(**dict_) # better solution


___ nt2json(nt
    r.. json.dumps(nt._asdict(), default=s..)

nt = dict2nt(blog)
print(nt.started)
print(t..(nt.started

print(t..(nt
print(json.dumps(nt._asdict(), default=s..