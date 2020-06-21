import inspect
from pprint import pprint
import linuxhint

person = linuxhint.Person(name='inspect_getmembers')
pprint(inspect.getmembers(person, inspect.ismethod))