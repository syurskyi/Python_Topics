# genfind.py
#
# A function that generates files that match a given filename pattern

from pathlib import Path

def gen_find(filepat, top):
    yield from Path(top).rglob(filepat)

# Example use

__ __name__ == '__main__':
    lognames = gen_find("access-log*","www")
    ___ name __ lognames:
        print(name)
