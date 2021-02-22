# retuple.py
#
# Read a sequence of log lines and parse them into a sequence of tuples

loglines = o..( *a..)

______ __

logpats  = r'(\S+) (\S+) (\S+) \[(.*?)\] ' \
           r'"(\S+) (\S+) (\S+)" (\S+) (\S+)'

logpat   = __.co..(logpats)

groups   = (logpat.m..(line) ___ line __ loglines)
tuples   = (g.groups() ___ g __ groups __ g)

__ __name__ __ '__main__':
    ___ t __ tuples:
        print(t)
