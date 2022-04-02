___ wc(file_
    """Takes an absolute file path/name, calculates the number of
       lines/words/chars, and returns a string of these numbers + file, e.g.:
       3 12 60 /tmp/somefile
       (both tabs and spaces are allowed as separator)"""
    w__ o.. file_ _ __ f:
        lines = f.r..


    number_of_lines = l..(lines)

    characters = 0
    words = 0
    ___ line __ lines:
        words +=  l..(line.s..
        characters += l..(line)


    r.. f"{number_of_lines} {words} {characters} {file_}"



__ _____ __ _____
    # make it work from cli like original unix wc
    _______ ___
    print(wc(___.argv[1]))
