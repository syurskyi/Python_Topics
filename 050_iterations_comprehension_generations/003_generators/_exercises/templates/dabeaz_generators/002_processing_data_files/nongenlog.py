# nongenlog.py
#
# Sum up the number of bytes transferred in an Apache log file
# using a simple for-loop.   We're not using generators here.

w___ o..( *a..) __ wwwlog:
    total = 0
    ___ line __ wwwlog:
        bytes_sent = line.rs..(N..,1)[1]
        __ bytes_sent != '-':
            total += in.(bytes_sent)
    print("Total", total)
