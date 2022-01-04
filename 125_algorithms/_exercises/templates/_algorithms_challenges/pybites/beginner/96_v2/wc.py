___ wc(file_):
    """Takes an absolute file path/name, calculates the number of
       lines/words/chars, and returns a string of these numbers + file, e.g.:
       3 12 60 /tmp/somefile
       (both tabs and spaces are allowed as separator)"""
    w__ open(file_,'r') __ f:
        lines = f.readlines()


    number_of_lines = l..(lines)

    characters = 0
    words = 0
    ___ line __ lines:
        words +=  l..(line.s..())
        characters += l..(line)


    r.. f"{number_of_lines} {words} {characters} {file_}"



__ _____ __ _____
    # make it work from cli like original unix wc
    _______ sys
    print(wc(sys.argv[1]))
