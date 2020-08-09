# Problem: https://www.hackerrank.com/challenges/sock-merchant/problem
# Score: 10


___ sock_merchant(ar
    list_of_socks = [0 ___ i in range(101)]
    ___ element in ar:
        list_of_socks[element] = list_of_socks[element] + 1
    ans = 0
    ___ sock in list_of_socks:
        ans += sock // 2
    r_ ans


n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = sock_merchant(ar)
print(result)
