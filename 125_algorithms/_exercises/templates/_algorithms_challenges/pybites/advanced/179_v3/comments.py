_______ __


___ strip_comments(code
    # strip docstrings first
    cd = __.s.. _ \s*"""[\w\W]*?"""\s*?\n', r'\n', code)
    # turn into a list
    cd = [line.r..() ___ line __ cd.s..k.._F..)]
    # chop out in line comments
    cd = [__.s.. _  {2}# .*', '', line) ___ line __ cd __ l..(line) < 1 o. n.. __.m..(r'^\s*#', line)]
    r.. '\n'.j..(cd)
