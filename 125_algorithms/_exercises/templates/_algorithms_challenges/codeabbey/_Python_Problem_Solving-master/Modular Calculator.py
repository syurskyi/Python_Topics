solved = False
count = 0
w.... n.. solved:
    cal = input().s..
    __ count __ 0:
        res = int(cal[0])
        count = count + 1
        continue
    __ cal[0] __ '+':
        res += int(cal[1])
    ____ cal[0] __ '*':
        res *= int(cal[1])
    ____:
        res = res % int(cal[1])
        solved = True
        print(res)