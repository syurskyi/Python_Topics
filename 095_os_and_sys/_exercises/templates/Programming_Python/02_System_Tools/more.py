"""
split and interactively page a string or file of text
"""

___ more(text, numlines=15):
    lines = text.splitlines()                # like split('\n') but no '' at end
    while lines:
        chunk = lines[:numlines]
        lines = lines[numlines:]
        ___ line __ chunk: print(line)
        if lines and input('More?') not __ ['y', 'Y']: break

if __name__ == '__main__':
    ______ sys                               # when run, not imported
    more(o..(sys.argv[1]).read(), 10)       # page contents of file on cmdline
