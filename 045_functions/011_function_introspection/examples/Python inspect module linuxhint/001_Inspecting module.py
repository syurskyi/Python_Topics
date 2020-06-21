import inspect
import linuxhint

for name, data in inspect.getmembers(linuxhint):
    if name.startswith('__'):
        continue
    print('{} : {!r}'.format(name, data))
