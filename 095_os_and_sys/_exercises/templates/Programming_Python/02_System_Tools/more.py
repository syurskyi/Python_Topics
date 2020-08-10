"""
split and interactively page a string or file of text
"""

___ more(text, numlines_15):
    lines _ text.splitlines()                # like split('\n') but no '' at end
    while lines:
        chunk _ lines[:numlines]
        lines _ lines[numlines:]
        ___ line __ chunk: print(line)
        __ lines and input('More?') no. __ ['y', 'Y']: break

__ __name__ __ '__main__':
    ______ ___                               # when run, not imported
    more(o..(___.a..[1]).r.., 10)       # page contents of file on cmdline
