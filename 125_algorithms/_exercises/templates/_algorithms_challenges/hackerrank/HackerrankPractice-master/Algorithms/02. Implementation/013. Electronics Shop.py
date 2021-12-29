# Problem https://www.hackerrank.com/challenges/electronics-shop/problem
# Score: 15


___ getMoneySpent(keyboards, drives, b):
    result = -1
    for i in range(1, len(keyboards)):
        for j in range(1, len(drives)):
            __ result < keyboards[i] + drives[j] <= b:
                result = keyboards[i] + drives[j]
    return result


b, n, m = map(int, input().split())
keyboards = list(map(int, input().rstrip().split()))
drives = list(map(int, input().rstrip().split()))
moneySpent = getMoneySpent(keyboards, drives, b)
print(moneySpent)
