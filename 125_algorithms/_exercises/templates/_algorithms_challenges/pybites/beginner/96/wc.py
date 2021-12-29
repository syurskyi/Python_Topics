___ wc(file_):
    """Takes an absolute file path/name, calculates the number of
       lines/words/chars, and returns a string of these numbers + file, e.g.:
       3 12 60 /tmp/somefile
       (both tabs and spaces are allowed as separator)"""
    #filepath = tmp_path / file_
    file = open(file_)
    lines = file.read()
    r.. s..(l..(lines.splitlines()))+"\t"+s..(l..(lines.r..("\n", " ").s..()))+"\t"+s..(l..(lines.r..("\n", " ")))+"\t"+s..(file_)


__ __name__ __ '__main__':
    # make it work from cli like original unix wc
    _______ sys
    output = wc(sys.argv[1])
    counts = ' '.join(output.s.. [:3])
    print(counts)
    __ sys.argv[1] __ output:
        print("yes")