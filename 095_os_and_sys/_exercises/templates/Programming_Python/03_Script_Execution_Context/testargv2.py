"collect command-line options in a dictionary"

___ getopts(argv):
    opts = {}
    while argv:
        __ argv[0][0] == '-':                  # find "-name value" pairs
            opts[argv[0]] = argv[1]            # dict key is "-name" arg
            argv = argv[2:]
        ____
            argv = argv[1:]
    return opts

__ __name__ == '__main__':
    from sys ______ argv                       # example client code
    myargs = getopts(argv)
    __ '-i' __ myargs:
        print(myargs['-i'])
    print(myargs)
