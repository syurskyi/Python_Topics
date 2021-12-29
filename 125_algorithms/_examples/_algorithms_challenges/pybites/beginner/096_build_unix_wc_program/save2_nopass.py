def wc(file_):
    f = open(file_, 'r')
    text = f.read()
    f.close()
    char = len(text)
    line = len(text.splitlines()) + 1
    word = len(text.split())
    return f'{line} {word} {char}'


if __name__ == '__main__':
    # make it work from cli like original unix wc
    import sys
    if len(sys.argv) > 1:
        print(wc(sys.argv[1:]))