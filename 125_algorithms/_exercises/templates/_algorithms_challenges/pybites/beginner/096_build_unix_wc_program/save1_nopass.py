___ wc(file_):
    f = open(file_, 'r')
    text = f.read()
    f.close()
    char = len(text)
    line = text.count('\n')
    word = len(text.split())
    return f'{line} {word} {char}'


__ __name__ == '__main__':
    # make it work from cli like original unix wc
    import sys
    __ len(sys.argv) > 1:
        print(wc(sys.argv[1:]))