print('#' * 52 + '  ### Not Just a Context Manager')

f = open('test.txt', 'w')
f.writelines('this is a test')
f.close()

print('#' * 52 + '  On the other hand we can also use it with a context manager:')

with open('test.txt') as f:
    print(f.readlines())

print('#' * 52 + '  We can implement classes that implement their own functionality'
                 '  as well as a context manager if we want to.')


class DataIterator:
    def __init__(self, fname):
        self._fname = fname
        self._f = None

    def __iter__(self):
        return self

    def __next__(self):
        row = next(self._f)
        return row.strip('\n').split(',')

    def __enter__(self):
        self._f = open(self._fname)
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        if not self._f.closed:
            self._f.close()
        return False

with DataIterator('nyc_parking_tickets_extract.csv') as data:
    for row in data:
        print(row)

print('#' * 52 + '  Of course, we cannot use this iterator without also using the context manager'
                 '  since the file would not be opened otherwise:')

data = DataIterator('nyc_parking_tickets_extract.csv')

# for row in data:
#     print(row)    # TypeError: 'NoneType' object is not an iterator

print('#' * 52 + '  But I want to point out that creating the context manager and using the `with` statement'
                 '  can be done in two steps if we want to:')

data_iter = DataIterator('nyc_parking_tickets_extract.csv')

with data_iter as data:
    for row in data:
        print(row)

