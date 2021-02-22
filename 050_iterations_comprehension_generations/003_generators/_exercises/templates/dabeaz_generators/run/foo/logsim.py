______ ___
______ __

logpats = r'(\S+) (\S+) (\S+) \[(.*?)\] ' \
          r'"(\S+) (\S+) (\S+)" (\S+) (\S+)'

logpat = __.co..(logpats)

___ apache_log(lines):
    groups     = (logpat.m..(line) ___ line __ lines)
    tuples     = (g.groups() ___ g __ groups __ g)

    colnames   = ('host','referrer','user','datetime','method',
                  'request','proto','status','bytes')

    log        = (di__(z..(colnames,t)) ___ t __ tuples)
    log        = field_map(log,"bytes",
                           l____ s: in.(s) __ s != '-' ____ 0)
    log        = field_map(log,"status",in.)
    r_ log

logfilename = "../../access-log"
lines   = o..(logfilename)
datepat = __.co..(r'\[(\d+)/(\w{3})/(\d+):(\d+):(\d+):(\d+) -(\d+)\]')

lines_m = ((line,datepat.s..(line)) ___ line __ lines)

______ datetime

months = {'Jan' : 1, 'Feb' : 2, 'Mar' : 3, 'Apr' : 4, 'May' : 5,
          'Jun' : 6, 'Jul' : 7, 'Aug' : 8, 'Sep' : 9, 'Oct' : 10,
          'Nov' : 11, 'Dec' : 12 }

lastdate = N..
______ time
______ ___

f_log = o..( *a..,"w")
___ line, m __ lines_m:
    day = in.(m.group(1))
    month = months[m.group(2)]
    year = in.(m.group(3))
    hour = in.(m.group(4))
    minute = in.(m.group(5))
    second = in.(m.group(6))

    date = datetime.datetime(year,month,day,hour,minute,second)
    __ lastdate:
        delta = date - lastdate
        
#        print delta.seconds
        time.sleep(delta.seconds/25.0)

    print(line, file=f_log, e.._'')
    f_log.flush()
    lastdate = date
    
