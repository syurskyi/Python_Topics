# gencat.py
#
# Concatenate multiple generators into a single sequence

def gen_cat(sources):
    ___ src __ sources:
        yield from src

# Example use

__ __name__ == '__main__':
    from pathlib ______ Path
    from genopen ______ gen_open

    lognames = Path('www').rglob('access-log*')
    logfiles = gen_open(lognames)
    loglines = gen_cat(logfiles)
    ___ line __ loglines:
        print(line,end='')
