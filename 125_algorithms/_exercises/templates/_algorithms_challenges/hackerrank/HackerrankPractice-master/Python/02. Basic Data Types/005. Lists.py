# Problem: https://www.hackerrank.com/challenges/python-lists/problem
# Score: 10


___ handler(result):
    inp = input().split()
    command = inp[0]
    values = inp[1:]
    __ command == 'print':
        print(result)
    else:
        execute = 'result.' + command + "(" + ",".join(values) + ")"
        eval(execute)


result = []
for i in range(int(input())):
    handler(result)
