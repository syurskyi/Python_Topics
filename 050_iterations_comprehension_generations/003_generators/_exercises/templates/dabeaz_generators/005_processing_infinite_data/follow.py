# follow.py
#
# Follow a file like tail -f.

______ time
______ os

___ follow(thefile):
    thefile.seek(0, os.SEEK_END)
    while True:
        line = thefile.readline()
        __ not line:
            time.sleep(0.1)
            continue
        y... line

# Example use
# Note : This example requires the use of an apache log simulator.
# 
# Go to the directory run/foo and run the program 'logsim.py' from
# that directory.   Run this program as a background process and
# leave it running in a separate window.  We'll write program
# that read the output file being generated
# 

__ __name__ __ '__main__':
    logfile = o..("run/foo/access-log","r")
    loglines = follow(logfile)
    ___ line __ loglines:
        print(line, e.._'')

    
