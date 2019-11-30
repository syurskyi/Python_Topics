import sys


def traceit(frame, event, arg):
    if event == "line":
        lineno = frame.f_lineno
        print("line", lineno)

    return traceit


def main():
    print("In main")
    for i in range(5):
        print(i, i * 3)
    print("Done.")


sys.settrace(traceit)
main()