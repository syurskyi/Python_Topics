# apachelog.py
#
# Parse an apache log file into a sequence of dictionaries

from fieldmap ______ field_map

______ re

logpats  = r'(\S+) (\S+) (\S+) \[(.*?)\] ' \
           r'"(\S+) (\S+) (\S+)" (\S+) (\S+)'

logpat   = re.compile(logpats)

def apache_log(lines):
    groups = (logpat.match(line) ___ line __ lines)
    tuples = (g.groups() ___ g __ groups __ g)
    
    colnames = ('host','referrer','user','datetime',
                'method', 'request','proto','status','bytes')

    log      = (dict(zip(colnames,t)) ___ t __ tuples)
    log      = field_map(log,"status",in.)
    log      = field_map(log,"bytes",
                         lambda s: in.(s) __ s != '-' else 0)

    return log

# Example use:

__ __name__ == '__main__':
    from linesdir ______ lines_from_dir
    lines = lines_from_dir("access-log*","www")
    log = apache_log(lines)
    ___ r __ log:
        print(r)


