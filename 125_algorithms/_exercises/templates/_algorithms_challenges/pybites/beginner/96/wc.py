___ wc(file_
    """Takes an absolute file path/name, calculates the number of
       lines/words/chars, and returns a string of these numbers + file, e.g.:
       3 12 60 /tmp/somefile
       (both tabs and spaces are allowed as separator)"""
    #filepath = tmp_path / file_
    file = o.. file_)
    lines = file.r..
    r.. s..(l..(lines.s..()))+"\t"+s..(l..(lines.r..("\n", " ").s..()))+"\t"+s..(l..(lines.r..("\n", " ")))+"\t"+s..(file_)


__ _____ __ _____
    # make it work from cli like original unix wc
    _______ ___
    output = wc(___.argv[1])
    counts = ' '.j..(output.s.. [:3])
    print(counts)
    __ ___.argv[1] __ output:
        print("yes")