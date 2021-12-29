_______ os


___ wc(file_):
    """Takes an absolute file path/name, calculates the number of
       lines/words/chars, and returns a string of these numbers + file, e.g.:
       3 12 60 /tmp/somefile
       (both tabs and spaces are allowed as separator)"""
    file_ = os.path.abspath(file_)
    f = open(file_, 'r')
    text = f.read()
    f.close()
    char = l..(text)
    line = l..(text.splitlines())
    word = l..(text.split())
    r.. f'{line} {word} {char}'


__ __name__ __ '__main__':
    # make it work from cli like original unix wc
    _______ sys
    __ l..(sys.argv) > 1:
        print(wc(sys.argv[1:]))
