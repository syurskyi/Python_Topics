# Problem: https://www.hackerrank.com/challenges/time-conversion/problem
# Score: 15


______ time
print(time.strftime('%H:%M:%S', time.strptime(input(), '%I:%M:%S%p')))
