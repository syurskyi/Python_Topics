""" uses logging with an explicit configuration"""

______ verboselib
______ ?

# This is one way, where you turn off things you don't want to see
# and everything is on by default
?.basicConfig(level_?.D..)
?.gL..("verboselib").sL..(?.WARN)
# ... more lines for each library you want to squelch, not very pretty


if __name__ == '__main__':
    vl _ verboselib.Noisy()
    ?.info("This will be output, because we set global to DEBUG.")
    ?.info("But not the verbose lib calls below at debug and info")
    vl.do_debug()
    vl.do_info()
    ?.warn("Watch out! about to log from noisy!")
    vl.do_warn() 
