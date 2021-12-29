import os


def wc(file_):
    """Takes an absolute file path/name, calculates the number of
       lines/words/chars, and returns a string of these numbers + file, e.g.:
       3 12 60 /tmp/somefile
       (both tabs and spaces are allowed as separator)"""
    file_name = os.path.abspath(file_)
    f = open(file_name, 'r')
    text = f.read()
    f.close()
    char = len(text)
    line = len(text.splitlines())
    word = len(text.split())
    return f'{line} {word} {char} /tmp/{file_name}'


if __name__ == '__main__':
    # make it work from cli like original unix wc
    import sys
    if len(sys.argv) > 1:
        print(wc(sys.argv[1:]))
