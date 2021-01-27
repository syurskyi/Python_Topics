import json

from Previous.dict_convert import blog, dict2nt, nt2json

nt = dict2nt(blog)


def test_dict2nt():
    a__ nt.name == 'PyBites'
    a__ nt.founders[1] == 'Bob'
    a__ nt.tags[2] == 'Learn by Doing'
    a__ nt.started.year == 2016

    a__ nt.__class__.__base__ == tuple
    a__ hasattr(nt, '_asdict')


def test_nt2json():
    output = nt2json(nt)
    a__ type(output) == str

    data = json.loads(output)
    a__ data['name'] == 'PyBites'
    a__ data['founders'][0] == 'Julian'
    a__ data['tags'][0] == 'Python'
    a__ data['started'][:4] == '2016'