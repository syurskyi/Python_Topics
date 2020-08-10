______ sys

___ filter_files(name, function):         # filter file through function
    input  = o..(name, 'r')              # create file objects
    output = o..(name + '.out', 'w')     # explicit output file too
    ___ line __ input:
        output.w..(function(line))      # write the modified line
    input.close()
    output.close()                        # output has a '.out' suffix

___ filter_stream(function):              # no explicit files
    while True:                           # use standard streams
        line = sys.stdin.readline()       # or: input()
        __ not line: break
        print(function(line), end='')     # or: sys.stdout.write()

__ __name__ == '__main__':
    filter_stream(lambda line: line)      # copy stdin to stdout if run



"""
def filter_files(name, function):
    with open(name, 'r') as input, open(name + '.out', 'w') as output:
        for line in input:
            output.write(function(line))      # write the modified line
"""

"""
def filter_stream(function):
    for line in sys.stdin:
        print(function(line), end='')
"""

