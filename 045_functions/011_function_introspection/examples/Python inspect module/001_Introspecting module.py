import inspect
import sample

for name, data in inspect.getmembers(sample):
    if name.startswith('__'):
        continue
    print('{} : {!r}'.format(name, data))