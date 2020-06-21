import inspect
from pprint import pprint
import sample

pprint(inspect.getmembers(sample.X, inspect.isfunction))