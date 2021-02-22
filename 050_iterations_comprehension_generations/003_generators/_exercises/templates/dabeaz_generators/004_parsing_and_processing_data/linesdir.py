# linesdir.py
#
# Generate a sequence of lines from files in a directory

f.. p_l_ ______ P..
f.. gencat ______ *
f.. genopen ______ *

___ lines_from_dir(filepat, dirname):
    names = P..(dirname).r_g_(filepat)
    files = gen_open(names)
    lines = gen_cat(files)
    r_ lines

# Example use

__ __name__ __ '__main__':
    loglines = lines_from_dir *a.. *w..
    ___ line __ loglines:
        print(line, e.._'')
