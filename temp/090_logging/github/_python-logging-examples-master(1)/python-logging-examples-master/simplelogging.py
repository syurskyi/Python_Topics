""" uses logging instead of prints, but no explicit logging config"""

______ verboselib
______ ?


if  -n == '__main__':
    vl _ verboselib.Noisy()
    ?.i..("This, and the logging from Noisy, will not be output.")
    ?.i..("because the default level is w..")
    vl.do_debug()
    vl.do_info()
    ?.w..("Watch out! about to log from noisy!")
    vl.do_warn() 
