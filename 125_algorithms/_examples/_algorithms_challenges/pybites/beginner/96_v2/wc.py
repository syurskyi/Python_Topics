def wc(file_):
    """Takes an absolute file path/name, calculates the number of
       lines/words/chars, and returns a string of these numbers + file, e.g.:
       3 12 60 /tmp/somefile
       (both tabs and spaces are allowed as separator)"""
    with open(file_,'r') as f:
        lines = f.r..


    number_of_lines = len(lines)

    characters = 0
    words = 0
    for line in lines:
        words +=  len(line.split())
        characters += len(line)


    return f"{number_of_lines} {words} {characters} {file_}"



if __name__ == '__main__':
    # make it work from cli like original unix wc
    import sys
    print(wc(sys.a.. 1
