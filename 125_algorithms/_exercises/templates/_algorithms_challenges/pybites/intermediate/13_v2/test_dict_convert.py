_______ json

____ dict_convert _______ blog, dict2nt, nt2json

nt = dict2nt(blog)


___ test_dict2nt
    ... nt.name __ 'PyBites'
    ... nt.founders[1] __ 'Bob'
    ... nt.tags[2] __ 'Learn by Doing'
    ... nt.started.year __ 2016

    ... nt.__class__.__base__ __ t..
    ... hasattr(nt, '_asdict')


___ test_nt2json
    output = nt2json(nt)
    ... t..(output) __ s..

    data = json.loads(output)
    ... data 'name'  __ 'PyBites'
    ... data 'founders' [0] __ 'Julian'
    ... data 'tags' [0] __ 'Python'
    ... data 'started' [:4] __ '2016'
