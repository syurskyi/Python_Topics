_______ os


___ wc(file_
    """Takes an absolute file path/name, calculates the number of
       lines/words/chars, and returns a string of these numbers + file, e.g.:
       3 12 60 /tmp/somefile
       (both tabs and spaces are allowed as separator)"""
    file_ = os.path.abspath(file_)
    f = o.. file_, 'r')
    text = f.r..
    f.close()
    char = l..(text)
    line = l..(text.s..())
    word = l..(text.s..())
    r.. f'{line} {word} {char}'


__ _____ __ _____
    # make it work from cli like original unix wc
    _______ sys
    __ l..(sys.argv) > 1:
        print(wc(sys.argv[1:]))
