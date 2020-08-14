# ______ ?
#
# # 1420811950.9472651 - INFO - elife-api - incoming - foo is in bar, making foobar
# # 1420811950.9472651 - INFO - lagotto - metrics - baz bar foo foo bar
# FORMAT _ ?.F..("_ cr.. f - _ l.. s - _ pN.. s - _ n.. s - _ m.. s"
# DEV_FORMAT _ ?.F..("_ cr.. f - _ l.. s - _ fN.. s:_ l_l_.. d - _ n.. s - _ m.. s"
#
# LOGFILE _ "./example.log"
# DEV_LOGFILE _ "example.dev.log"
#
# # http://docs.python.org/2/howto/logging-cookbook.html
# logger _ ?.gL..("") # important! this is the *root logger*
#                                # all other loggers are derived from this one
# ?.sL.. ?.D.. # *default* output level
#
# # StreamHandler sends to stderr by default
# ? _ ?.SH..
# ?.sL.. ?.I.. # output level for *this handler*
# ?.sF.. F..
#
# # FileHandler sends to a named file
# h2 _ ?.FH.. L..
# h2.sL.. ?.W.. # change to INFO __ code is less-than-stable
# h2.sF.. F..
#
# # outputs *everything* to a seperate file, good for debugging during dev
# h3 _ ?.FH.. D..
# # h3.setLevel(logging.DEBUG) # not neccessary as the root logger outputs at DEBUG
# h3.sF..(D.. # for dev you might want a friendlier logging format
#
# ?.aH..(?)
# ?.aH..(h2)
# ?.aH..(h3)
#
# ?.d..("configuration loaded")
