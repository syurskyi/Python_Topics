"""
split and interactively page a string or file of text
"""

___ more(text, numlines_15):
    lines _ text.splitlines()                # like split('\n') but no '' at end
    while lines:
        chunk _ lines[:numlines]
        lines _ lines[numlines:]
        ___ line __ chunk: print(line)
        __ lines and input('More?') not __ ['y', 'Y']: break

__ __name__ == '__main__':
    ______ ___                               # when run, not imported
    more(o..(___.argv[1]).read(), 10)       # page contents of file on cmdline
