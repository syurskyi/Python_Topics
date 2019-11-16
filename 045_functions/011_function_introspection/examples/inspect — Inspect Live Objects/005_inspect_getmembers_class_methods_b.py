import inspect
from pprint import pprint

import example

pprint(inspect.getmembers(example.B, inspect.isfunction))
