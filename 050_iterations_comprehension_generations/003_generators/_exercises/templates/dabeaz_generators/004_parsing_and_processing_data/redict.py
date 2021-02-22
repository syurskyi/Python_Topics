# redict.py
#
# Read a sequence of log lines and parse them into a sequence of dictionaries

loglines = o..( *a..)

______ re

logpats  = r'(\S+) (\S+) (\S+) \[(.*?)\] ' \
           r'"(\S+) (\S+) (\S+)" (\S+) (\S+)'

logpat   = re.compile(logpats)

groups   = (logpat.match(line) ___ line __ loglines)
tuples   = (g.groups() ___ g __ groups __ g)

colnames = ('host','referrer','user','datetime',
            'method', 'request','proto','status','bytes')

log      = (dict(zip(colnames, t)) ___ t __ tuples)

__ __name__ == '__main__':
    ___ x __ log:
        print(x)
