# genopen.py
#
# Takes a sequence of filenames as input and yields a sequence of file
# objects that have been suitably open

import gzip, bz2

def gen_open(paths):
    ___ path __ paths:
        __ path.suffix == '.gz':
            yield gzip.o..(path, 'rt')
        elif path.suffix == '.bz2':
            yield bz2.o..(path, 'rt')
        else:
            yield o..(path, 'rt')

# Example use

__ __name__ == '__main__':
    from pathlib import Path
    lognames = Path('www').rglob('access-log*')
    logfiles = gen_open(lognames)
    ___ f __ logfiles:
        print(f)
