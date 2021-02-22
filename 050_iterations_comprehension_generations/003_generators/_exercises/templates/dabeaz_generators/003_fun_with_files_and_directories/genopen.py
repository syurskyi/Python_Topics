# genopen.py
#
# Takes a sequence of filenames as input and yields a sequence of file
# objects that have been suitably open

______ gzip, bz2

___ gen_open(paths):
    ___ path __ paths:
        __ path.suffix == '.gz':
            y... gzip.o..(path, 'rt')
        elif path.suffix == '.bz2':
            y... bz2.o..(path, 'rt')
        else:
            y... o..(path, 'rt')

# Example use

__ __name__ == '__main__':
    f.. p_l_ ______ P..
    lognames = P..('www').r_g_('access-log*')
    logfiles = gen_open(lognames)
    ___ f __ logfiles:
        print(f)
