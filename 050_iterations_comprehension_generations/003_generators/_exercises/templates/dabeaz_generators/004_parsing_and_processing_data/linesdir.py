# linesdir.py
#
# Generate a sequence of lines from files in a directory

from pathlib ______ Path
from gencat ______ *
from genopen ______ *

def lines_from_dir(filepat, dirname):
    names = Path(dirname).rglob(filepat)
    files = gen_open(names)
    lines = gen_cat(files)
    return lines

# Example use

__ __name__ == '__main__':
    loglines = lines_from_dir("access-log*","www")
    ___ line __ loglines:
        print(line, end='')
