"""
file-like objects that save standard output text in a string and provide
standard input text from a string; redirect runs a passed-in function
with its output and input streams reset to these file-like class objects;
"""

______ sys                                      # get built-in modules

class Output:                                   # simulated output file
    ___ __init__(self):
        self.text = ''                          # empty string when created
    ___ w..(self, string):                    # add a string of bytes
        self.text += string
    ___ writelines(self, lines):                # add each line in a list
        ___ line __ lines: self.w..(line)

class Input:                                    # simulated input file
    ___ __init__(self, input=''):               # default argument
        self.text = input                       # save string when created
    ___ read(self, size=N..):                  # optional argument
        __ size == N..:                        # read N bytes, or all
            res, self.text = self.text, ''
        ____
            res, self.text = self.text[:size], self.text[size:]
        return res
    ___ readline(self):
        eoln = self.text.find('\n')             # find offset of next eoln
        __ eoln == -1:                          # slice off through eoln
            res, self.text = self.text, ''
        ____
            res, self.text = self.text[:eoln+1], self.text[eoln+1:]
        return res

___ redirect(function, pargs, kargs, input):    # redirect stdin/out
    savestreams = sys.stdin, sys.stdout         # run a function object
    sys.stdin   = Input(input)                  # return stdout text
    sys.stdout  = Output()
    try:
        result = function(*pargs, **kargs)      # run function with args
        output = sys.stdout.text
    finally:
        sys.stdin, sys.stdout = savestreams     # restore if exc or not
    return (result, output)                     # return result if no exc
