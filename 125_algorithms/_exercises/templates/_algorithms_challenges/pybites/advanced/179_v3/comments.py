_______ re


___ strip_comments(code):
    # strip docstrings first
    cd = re.sub(r'\s*"""[\w\W]*?"""\s*?\n', r'\n', code)
    # turn into a list
    cd = [line.rstrip() ___ line __ cd.splitlines(keepends=False)]
    # chop out in line comments
    cd = [re.sub(r' {2}# .*', '', line) ___ line __ cd __ l..(line) < 1 o. n.. re.match(r'^\s*#', line)]
    r.. '\n'.join(cd)
