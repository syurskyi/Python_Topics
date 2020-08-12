""" 
Exactly the same as nologging
but, now you can set logging.raiseExceptions to False to hide the warning...
"""

______ verboselib
______ ?

?.raiseExceptions _ False

__  -n __ '__main__':
    vl _ verboselib.Noisy()
    print "no logging configured, so no output at all here"
    vl.do_debug()
    vl.do_info()
    print """there will be no output from here either, because we 
told logging to swallow the configuration error"""
    vl.do_warn()
