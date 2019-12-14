# While you can pass any variable that can be represented as a string from your program as a message to your logs,
# there are some basic elements that are already a part of the LogRecord and can be easily added to the output format.
# If you want to log the process ID along with the level and message, you can do something like this:

______ l____

l____.basicConfig(format='%(process)d-%(levelname)s-%(message)s')
l____.warning('This is a Warning')
# 18472-WARNING-This is a Warning

# format can take a string with LogRecord attributes in any arrangement you like. The entire list of available
# attributes can be found here.
#
# Here is another example where you can add the date and time info:

______ l____

l____.basicConfig(format='%(asctime)s - %(message)s', level=l____.INFO)
l____.info('Admin logged in')
# 2018-07-11 20:12:06,288 - Admin logged in

# %(asctime)s adds the time of creation of the LogRecord. The format can be changed using the datefmt attribute,
# which uses the same formatting language as the formatting functions in the datetime module, such as time.strftime():

______ l____

l____.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
l____.warning('Admin logged out')
# 12-Jul-18 20:53:19 - Admin logged out
# You can find the guide here.