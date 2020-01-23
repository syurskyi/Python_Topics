# The trace module helps you understand the way your program runs. You can trace the statements executed,
# produce coverage reports, and investigate the relationships between functions that call each other.
#
# Command Line Interface
# It is easy use trace directly from the command line. Given the following Python scripts as input:

from recurse import recurse

def main():
    print 'This is the main program.'
    recurse(2)
    return

if __name__ == '__main__':
    main()
def recurse(level):
    print 'recurse(%s)' % level
    if level:
        recurse(level-1)
    return

def not_called():
    print 'This function is never called.'

# Tracing Execution
# We can see which statements are being executed as the program runs using the --trace option.
#
# $ python -m trace --trace trace_example/main.py
#
#  --- modulename: main, funcname: <module>
# main.py(7): """
# main.py(12): from recurse import recurse
#  --- modulename: recurse, funcname: <module>
# recurse.py(7): """
# recurse.py(12): def recurse(level):
# recurse.py(18): def not_called():
# main.py(14): def main():
# main.py(19): if __name__ == '__main__':
# main.py(20):     main()
#  --- modulename: main, funcname: main
# main.py(15):     print 'This is the main program.'
# This is the main program.
# main.py(16):     recurse(2)
#  --- modulename: recurse, funcname: recurse
# recurse.py(13):     print 'recurse(%s)' % level
# recurse(2)
# recurse.py(14):     if level:
# recurse.py(15):         recurse(level-1)
#  --- modulename: recurse, funcname: recurse
# recurse.py(13):     print 'recurse(%s)' % level
# recurse(1)
# recurse.py(14):     if level:
# recurse.py(15):         recurse(level-1)
#  --- modulename: recurse, funcname: recurse
# recurse.py(13):     print 'recurse(%s)' % level
# recurse(0)
# recurse.py(14):     if level:
# recurse.py(16):     return
# recurse.py(16):     return
# recurse.py(16):     return
# main.py(17):     return
#  --- modulename: trace, funcname: _unsettrace
# trace.py(80):         sys.settrace(None)
# The first part of the output shows some setup operations performed by trace. The rest of the output shows
# the entry into each function, including the module where the function is located, and then the lines of the source
# file as they are executed. You can see that recurse() is entered three times, as you would expect from the way it is
# called in main().