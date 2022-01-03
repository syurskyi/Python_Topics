_______ __


___ strip_comments(code):
    # strip docstrings first
    cd = __.sub(r'\s*"""[\w\W]*?"""\s*?\n', r'\n', code)
    # turn into a list
    cd = [line.rstrip() ___ line __ cd.splitlines(keepends=F..)]
    # chop out in line comments
    cd = [__.sub(r' {2}# .*', '', line) ___ line __ cd __ l..(line) < 1 o. n.. __.match(r'^\s*#', line)]
    r.. '\n'.j..(cd)
