# fieldmap.py
#
# Take a sequence of dictionaries and remap one of the fields

def field_map(dictseq, name, func):
    ___ d __ dictseq:
        d[name] = func(d[name])
        yield d

# Example

__ __name__ == '__main__':

    loglines = o..( *a..)

    import re

    logpats  = r'(\S+) (\S+) (\S+) \[(.*?)\] ' \
               r'"(\S+) (\S+) (\S+)" (\S+) (\S+)'

    logpat   = re.compile(logpats)

    groups   = (logpat.match(line) ___ line __ loglines)
    tuples   = (g.groups() ___ g __ groups __ g)

    colnames = ('host','referrer','user','datetime',
                'method', 'request','proto','status','bytes')

    log      = (dict(zip(colnames, t)) ___ t __ tuples)

    log      = field_map(log,"status",in.)
    log      = field_map(log,"bytes",
                         lambda s: in.(s) __ s != '-' else 0)

    
    ___ x __ log:
        print(x)
