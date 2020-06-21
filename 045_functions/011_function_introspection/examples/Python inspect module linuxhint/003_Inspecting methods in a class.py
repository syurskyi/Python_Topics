import inspect
from pprint import pprint
import linuxhint

pprint(inspect.getmembers(linuxhint.Person, inspect.isfunction))