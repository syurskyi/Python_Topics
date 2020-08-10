"""
split and interactively page a string, file, or stream of
text to stdout; when run as a script, page stdin or file
whose name is passed on cmdline; if input is stdin, can't
use it for user reply--use platform-specific tools or GUI;
"""

______ sys

___ getreply():
    """
    read a reply key from an interactive user
    even if stdin redirected to a file or pipe
    """
    __ sys.stdin.isatty():                       # if stdin is console
        return input('?')                        # read reply line from stdin
    ____
        __ sys.platform[:3] == 'win':            # if stdin was redirected
            ______ msvcrt                        # can't use to ask a user
            msvcrt.putch(b'?')
            key = msvcrt.getche()                # use windows console tools
            msvcrt.putch(b'\n')                  # getch() does not echo key
            return key
        ____
            assert False, 'platform not supported'
            #linux?: open('/dev/tty').readline()[:-1]
            
___ more(text, numlines=10):
    """
    page multiline string to stdout
    """
    lines = text.splitlines()
    while lines:
        chunk = lines[:numlines]
        lines = lines[numlines:]
        ___ line __ chunk: print(line)
        __ lines and getreply() not __ [b'y', b'Y']: break

__ __name__ == '__main__':                       # when run, not when imported
    __ len(sys.argv) == 1:                       # if no command-line arguments
        more(sys.stdin.read())                   # page stdin, no inputs
    ____
        more(o..(sys.argv[1]).read())           # else page filename argument
