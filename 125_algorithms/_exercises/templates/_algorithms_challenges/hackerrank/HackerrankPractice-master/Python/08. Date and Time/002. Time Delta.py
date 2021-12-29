# Problem: https://www.hackerrank.com/challenges/python-time-delta/problem
# Score: 30


____ d__ _______ d__ as dt

fmt = '%a %d %b %Y %H:%M:%S %z'
___ _ __ r..(int(input())):
    time1 = dt.strptime(input(), fmt)
    time2 = dt.strptime(input(), fmt)
    print(int(abs((time1 - time2).total_seconds())))
