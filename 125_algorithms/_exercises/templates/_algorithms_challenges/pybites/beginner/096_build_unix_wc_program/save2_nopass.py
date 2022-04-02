___ wc(file_
    f = o.. file_, 'r')
    text = f.r..
    f.close()
    char = l..(text)
    line = l..(text.s..()) + 1
    word = l..(text.s..())
    r.. f'{line} {word} {char}'


__ _____ __ _____
    # make it work from cli like original unix wc
    _______ sys
    __ l..(sys.argv) > 1:
        print(wc(sys.argv[1:]))