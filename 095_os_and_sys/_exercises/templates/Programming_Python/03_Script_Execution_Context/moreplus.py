"""
split and interactively page a string, file, or stream of
text to stdout; when run as a script, page stdin or file
whose name is passed on cmdline; if input is stdin, can't
use it for user reply--use platform-specific tools or GUI;
"""

______ ___

___ getreply():
    """
    read a reply key from an interactive user
    even if stdin redirected to a file or pipe
    """
    __ ___.stdin.isatty():                       # if stdin is console
        return input('?')                        # read reply line from stdin
    ____
        __ ___.platform[:3] __ 'win':            # if stdin was redirected
            ______ msvcrt                        # can't use to ask a user
            msvcrt.putch(b'?')
            key _ msvcrt.getche()                # use windows console tools
            msvcrt.putch(b'\n')                  # getch() does not echo key
            return key
        ____
            assert False, 'platform not supported'
            #linux?: open('/dev/tty').readline()[:-1]
            
___ more(text, numlines_10):
    """
    page multiline string to stdout
    """
    lines _ text.splitlines()
    while lines:
        chunk _ lines[:numlines]
        lines _ lines[numlines:]
        ___ line __ chunk: print(line)
        __ lines and getreply() not __ [b'y', b'Y']: break

__ __name__ __ '__main__':                       # when run, not when imported
    __ le.(___.a..) __ 1:                       # if no command-line arguments
        more(___.stdin.read())                   # page stdin, no inputs
    ____
        more(o..(___.a..[1]).read())           # else page filename argument
