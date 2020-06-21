import inspect
import linuxhint

for key, data in inspect.getmembers(linuxhint, inspect.isclass):
    print('{} : {!r}'.format(key, data))

