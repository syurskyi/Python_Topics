"collect command-line options in a dictionary"

___ getopts(a..):
    opts _ {}
    w__ a..:
        __ a..[0][0] __ '-':                  # find "-name value" pairs
            opts[a..[0]] _ a..[1]            # dict key is "-name" arg
            a.. _ a..[2:]
        ____
            a.. _ a..[1:]
    r_ opts

__ __name__ __ '__main__':
    ____ ___ ______ a..                       # example client code
    myargs _ getopts(a..)
    __ '-i' __ myargs:
        print(myargs['-i'])
    print(myargs)
