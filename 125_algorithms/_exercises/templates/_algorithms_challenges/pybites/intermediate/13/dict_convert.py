from collections import namedtuple
from datetime import datetime
import json


blog = dict(name='PyBites',
            founders=('Julian', 'Bob'),
            started=datetime(year=2016, month=12, day=19),
            tags=['Python', 'Code Challenges', 'Learn by Doing'],
            location='Spain/Australia',
            site='https://pybit.es')

# define namedtuple here
blog_nt = namedtuple("Blog", "name founders started tags location site")

___ dict2nt(dict_):
    nt = blog_nt._make([
        dict_["name"],
        dict_["founders"],
        dict_["started"],
        dict_["tags"],
        dict_["location"],
        dict_["site"]
    ])
    return nt


___ nt2json(nt):
    return json.dumps(nt._asdict(), indent=4, default=str)

# if __name__ == "__main__":
#     print(dict2nt(blog))
#     print(nt2json(dict2nt(blog)))