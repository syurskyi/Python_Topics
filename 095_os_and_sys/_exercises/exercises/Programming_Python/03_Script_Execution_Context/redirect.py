"""
file-like objects that save standard output text in a string and provide
standard input text from a string; redirect runs a passed-in function
with its output and input streams reset to these file-like class objects;
"""

______ ___                                      # get built-in modules

class Output:                                   # simulated output file
    ___ __init__(self):
        self.text _ ''                          # empty string when created
    ___ w..(self, string):                    # add a string of bytes
        self.text +_ string
    ___ writelines(self, lines):                # add each line in a list
        ___ line __ lines: self.w..(line)

class Input:                                    # simulated input file
    ___ __init__(self, input_''):               # default argument
        self.text _ input                       # save string when created
    ___ read(self, size_N..):                  # optional argument
        __ size __ N..:                        # read N bytes, or all
            res, self.text _ self.text, ''
        ____
            res, self.text _ self.text[:size], self.text[size:]
        r_ res
    ___ readline(self):
        eoln _ self.text.find('\n')             # find offset of next eoln
        __ eoln __ -1:                          # slice off through eoln
            res, self.text _ self.text, ''
        ____
            res, self.text _ self.text[:eoln+1], self.text[eoln+1:]
        r_ res

___ redirect(function, pargs, kargs, input):    # redirect stdin/out
    savestreams _ ___.stdin, ___.stdout         # run a function object
    ___.stdin   _ Input(input)                  # return stdout text
    ___.stdout  _ Output()
    ___
        result _ function(*pargs, **kargs)      # run function with args
        output _ ___.stdout.text
    finally:
        ___.stdin, ___.stdout _ savestreams     # restore if exc or not
    r_ (result, output)                     # return result if no exc
