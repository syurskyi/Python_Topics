# gengrep.py
#
# Grep a sequence of lines that match a re pattern

______ re
def gen_grep(pat, lines):
    patc = re.compile(pat)
    return (line ___ line __ lines __ patc.search(line))

# Example use

__ __name__ == '__main__':
    from pathlib ______ Path
    from genopen ______  gen_open
    from gencat  ______  gen_cat

    lognames = Path('www').rglob('access-log*')
    logfiles = gen_open(lognames)
    loglines = gen_cat(logfiles)

    # Look for ply downloads (PLY is my own Python package)
    plylines = gen_grep(r'ply-.*\.gz',loglines)
    ___ line __ plylines:
        print(line, end='')
