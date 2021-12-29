""" TASK DESCRIPTION:
Write a function to convert the given blog dict to a namedtuple.
Write a second function to convert the resulting namedtuple to json.
Here you probably need to use 2 of the _ methods of namedtuple :)
"""

from collections import namedtuple
from collections import OrderedDict
from datetime import datetime
import json

# Q: What is the difference between tuple and list?

blog = dict(name='PyBites',
            founders=('Julian', 'Bob'),
            started=datetime(year=2016, month=12, day=19),
            tags=['Python', 'Code Challenges', 'Learn by Doing'],
            location='Spain/Australia',
            site='https://pybit.es')
""" INITIAL CONSIDERATIONS:

How could resulting JSON look like? Question is how to serialize datetime?

j = { "name": "PyBites",
      "founders": ["Julian", "Bob"],
      "started": {
                    "year": "2016",
                    "month": "12",
                    "day": "19"
                },
      "tags": ["Python", "Code Challenges", "Learn by Doing"],
      "location": "Spain/Australia",
      "site": "https://pybit.es"
}
"""

### --------- My solution -------------

# define namedtuple here
Blog = namedtuple('Blog', 'name founders started tags location site')

def dict2nt(dict_):
    b = Blog(dict_.get('name'), dict_.get('founders'), dict_.get('started'), dict_.get('tags'), dict_.get('location'), dict_.get('site'))
    return b

def nt2json(nt):
    json.dump()


b = dict2nt(blog)
# Q: How to serialize datetime object?
# https://code-maven.com/serialize-datetime-object-as-json-in-python
# https://stackoverflow.com/questions/11875770/how-to-overcome-datetime-datetime-not-json-serializable/36142844#36142844
print(json.dumps(OrderedDict(b._asdict()), default=str, indent=4))


### ---------- PyBites original solution ---------------

# define namedtuple here
pybBlog = namedtuple('pybBlog', blog.keys())

# https://stackoverflow.com/questions/36901/what-does-double-star-asterisk-and-star-asterisk-do-for-parameters
def pyb_dict2nt(dict_):
    return pybBlog(**dict_)


def pyb_nt2json(nt):
    nt = nt._replace(started=str(nt.started))
    return json.dumps(nt._asdict())