___ wc(file_):
    f = open(file_, 'r')
    text = f.read()
    f.close()
    char = l..(text)
    line = l..(text.splitlines()) + 1
    word = l..(text.split())
    r.. f'{line} {word} {char}'


__ __name__ __ '__main__':
    # make it work from cli like original unix wc
    _______ sys
    __ l..(sys.argv) > 1:
        print(wc(sys.argv[1:]))