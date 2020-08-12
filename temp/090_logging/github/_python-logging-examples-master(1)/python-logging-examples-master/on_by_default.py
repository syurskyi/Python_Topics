""" uses logging with an explicit configuration"""

______ verboselib
______ ?

# This is one way, where you turn off things you don't want to see
# and everything is on by default
?.basicConfig(level_?.D..)
?.gL..("verboselib").sL..(?.WARN)
# ... more lines for each library you want to squelch, not very pretty


__  -n == '__main__':
    vl _ verboselib.Noisy()
    ?.i..("This will be output, because we set global to DEBUG.")
    ?.i..("But not the verbose lib calls below at d.. and i..")
    vl.do_debug()
    vl.do_info()
    ?.w..("Watch out! about to log from noisy!")
    vl.do_warn() 
