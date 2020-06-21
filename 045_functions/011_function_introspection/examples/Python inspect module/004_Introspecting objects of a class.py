import inspect
from pprint import pprint
import sample

x = sample.X(name='inspect_getmembers')
pprint(inspect.getmembers(x, inspect.ismethod))