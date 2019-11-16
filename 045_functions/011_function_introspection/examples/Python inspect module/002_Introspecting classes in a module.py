import inspect
import sample

for key, data in inspect.getmembers(sample, inspect.isclass):
    print('{} : {!r}'.format(key, data))