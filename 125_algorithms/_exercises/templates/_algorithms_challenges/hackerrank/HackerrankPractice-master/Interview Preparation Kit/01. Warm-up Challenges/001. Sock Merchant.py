# Problem: https://www.hackerrank.com/challenges/sock-merchant/problem
# Score: 10


___ sock_merchant(ar):
    list_of_socks = [0 ___ i __ r..(101)]
    ___ element __ ar:
        list_of_socks[element] = list_of_socks[element] + 1
    ans = 0
    ___ sock __ list_of_socks:
        ans += sock // 2
    r.. ans


n = i..(input().strip())
ar = l..(map(i.., input().s...s..(' ')))
result = sock_merchant(ar)
print(result)
