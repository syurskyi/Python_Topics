# fieldmap.py
#
# Take a sequence of dictionaries and remap one of the fields

___ field_map(dictseq, name, func):
    ___ d __ dictseq:
        d[name] = func(d[name])
        y... d

# Example

__ __name__ __ '__main__':

    loglines = o..( *a..)

    ______ re

    logpats  = r'(\S+) (\S+) (\S+) \[(.*?)\] ' \
               r'"(\S+) (\S+) (\S+)" (\S+) (\S+)'

    logpat   = re.co..(logpats)

    groups   = (logpat.m..(line) ___ line __ loglines)
    tuples   = (g.groups() ___ g __ groups __ g)

    colnames = ('host','referrer','user','datetime',
                'method', 'request','proto','status','bytes')

    log      = (di__(z..(colnames, t)) ___ t __ tuples)

    log      = field_map(log,"status",in.)
    log      = field_map(log,"bytes",
                         l____ s: in.(s) __ s != '-' ____ 0)

    
    ___ x __ log:
        print(x)
