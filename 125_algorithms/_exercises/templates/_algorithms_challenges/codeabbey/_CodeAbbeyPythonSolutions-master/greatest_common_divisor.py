amount_values = int(input())
results = []

___ gcd(num1, num2
    __(num2 __ 0
        r_ num1
    ____
        num1, num2 = num2, (num1%num2)
        r_(gcd(num1, num2))

___ lcm(num1, num2
    r_ num1*num2 // gcd(num1,num2)

___ get_lcm_and_gcd(num1,num2
    r_ "("+str(gcd(num1,num2))+" "+ str(lcm(num1, num2))+")"

___ i in range(amount_values
    num1, num2 = map(int, input().split())
    results.append(get_lcm_and_gcd(num1,num2))

print(*results)


