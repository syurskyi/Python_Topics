amount_values = int(input())
results    # list

___ gcd(num1, num2):
    __(num2 __ 0):
        r.. num1
    ____:
        num1, num2 = num2, (num1%num2)
        r..(gcd(num1, num2))

___ lcm(num1, num2):
    r.. num1*num2 // gcd(num1,num2)

___ get_lcm_and_gcd(num1,num2):
    r.. "("+s..(gcd(num1,num2))+" "+ s..(lcm(num1, num2))+")"

___ i __ r..(amount_values):
    num1, num2 = map(int, input().s..())
    results.a..(get_lcm_and_gcd(num1,num2))

print(*results)


