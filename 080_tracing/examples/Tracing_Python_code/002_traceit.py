import sys
import linecache


def traceit(frame, event, arg):
    if event == "line":
        lineno = frame.f_lineno
        line = linecache.getline("traceit.py", lineno)
        print("line %d: %s" % (lineno, line.rstrip()))
    return traceit


def main():
    print("In main")
    for i in range(5):
        print(i, i * 3)
    print("Done.")


sys.settrace(traceit)
main()