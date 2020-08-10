___ scanner(name, function):
    file _ o..(name, 'r')               # create a file object
    w__ True:
        line _ file.readline()           # call file methods
        __ no. line: break               # until end-of-file
        function(line)                   # call a function object
    file.close()


"""
def scanner(name, function):
    for line in open(name, 'r'):         # scan line by line
        function(line)                   # call a function object
"""


"""
def scanner(name, function):
    [function(line) for line in open(name, 'r')]
"""
