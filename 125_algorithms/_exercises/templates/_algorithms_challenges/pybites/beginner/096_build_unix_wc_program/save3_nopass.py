___ wc(file_):
    f = open(file_, 'r')
    text = f.read()
    f.close()
    char = l..(text)
    line = l..(text.splitlines())
    word = l..(text.s..())
    r.. f'{line} {word} {char}'


__ _____ __ _____
    # make it work from cli like original unix wc
    _______ sys
    __ l..(sys.argv) > 1:
        print(wc(sys.argv[1:]))