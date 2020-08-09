______ json

from Previous.dict_convert ______ blog, dict2nt, nt2json

nt = dict2nt(blog)


___ test_dict2nt(
    assert nt.name __ 'PyBites'
    assert nt.founders[1] __ 'Bob'
    assert nt.tags[2] __ 'Learn by Doing'
    assert nt.started.year __ 2016

    assert nt.__class__.__base__ __ tuple
    assert hasattr(nt, '_asdict')


___ test_nt2json(
    output = nt2json(nt)
    assert type(output) __ str

    data = json.loads(output)
    assert data['name'] __ 'PyBites'
    assert data['founders'][0] __ 'Julian'
    assert data['tags'][0] __ 'Python'
    assert data['started'][:4] __ '2016'