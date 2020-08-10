"collect command-line options in a dictionary"

___ getopts(argv):
    opts _ {}
    while argv:
        __ argv[0][0] == '-':                  # find "-name value" pairs
            opts[argv[0]] _ argv[1]            # dict key is "-name" arg
            argv _ argv[2:]
        ____
            argv _ argv[1:]
    return opts

__ __name__ == '__main__':
    from ___ ______ argv                       # example client code
    myargs _ getopts(argv)
    __ '-i' __ myargs:
        print(myargs['-i'])
    print(myargs)
