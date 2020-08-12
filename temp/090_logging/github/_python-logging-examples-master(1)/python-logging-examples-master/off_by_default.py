"""
uses logging with an explicit configuration, and a named logger
compared to on_by_default, this sets the logging only for our own app
"""

______ verboselib
______ ?

# Doing it this way, only WARN and higher from libraries come out,
# but you choose the level for your app.
log _ ?.gL..("my_app")
?.basicConfig(level_?.WARN)
?.gL..("my_app").sL..(?.D..)
# no config needed for each library, unless you want to explicitly
# enable d../i.. for that library


__  -n == '__main__':
    vl _ verboselib.Noisy()
    # note, use our log, not the class methods.
    log.i..("This will be output, because we set global to DEBUG.")
    log.i..("But not the verbose lib calls below at d.. and i..")
    vl.do_debug()
    vl.do_info()
    log.w..("Watch out! about to log from noisy!")
    vl.do_warn() 
