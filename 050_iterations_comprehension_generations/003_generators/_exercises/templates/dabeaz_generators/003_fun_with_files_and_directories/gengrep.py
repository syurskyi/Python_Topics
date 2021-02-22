# gengrep.py
#
# Grep a sequence of lines that match a re pattern

______ re
___ gen_grep(pat, lines):
    patc = re.compile(pat)
    return (line ___ line __ lines __ patc.search(line))

# Example use

__ __name__ == '__main__':
    f.. p_l_ ______ P..
    f.. genopen ______  gen_open
    f.. gencat  ______  gen_cat

    lognames = P..('www').r_g_('access-log*')
    logfiles = gen_open(lognames)
    loglines = gen_cat(logfiles)

    # Look for ply downloads (PLY is my own Python package)
    plylines = gen_grep(r'ply-.*\.gz',loglines)
    ___ line __ plylines:
        print(line, e.._'')
