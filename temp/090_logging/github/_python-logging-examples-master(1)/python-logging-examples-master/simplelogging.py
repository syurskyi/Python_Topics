""" uses logging instead of prints, but no explicit logging config"""

______ verboselib
______ ?


if __name__ == '__main__':
    vl _ verboselib.Noisy()
    ?.info("This, and the logging from Noisy, will not be output.")
    ?.info("because the default level is warn")
    vl.do_debug()
    vl.do_info()
    ?.warn("Watch out! about to log from noisy!")
    vl.do_warn() 
