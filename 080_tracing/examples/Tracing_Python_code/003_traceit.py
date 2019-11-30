import sys
import linecache
import random

def traceit(frame, event, arg):
    if event == "line":
        lineno = frame.f_lineno
        filename = frame.f_globals["__file__"]
        print("file %s line %d" % (filename, lineno))
    return traceit


def main():
    print("In main")
    for i in range(5):
        print(i, random.randrange(0, 10))
    print("Done.")

sys.settrace(traceit)
main()