def wc(file_):
    """Takes an absolute file path/name, calculates the number of
       lines/words/chars, and returns a string of these numbers + file, e.g.:
       3 12 60 /tmp/somefile
       (both tabs and spaces are allowed as separator)"""
    #filepath = tmp_path / file_
    file = open(file_)
    lines = file.read()
    return str(len(lines.splitlines()))+"\t"+str(len(lines.replace("\n", " ").split()))+"\t"+str(len(lines.replace("\n", " ")))+"\t"+str(file_)


if __name__ == '__main__':
    # make it work from cli like original unix wc
    import sys
    output = wc(sys.argv[1])
    counts = ' '.join(output.split()[:3])
    print(counts)
    if sys.argv[1] in output:
        print("yes")