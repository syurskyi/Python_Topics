# Problem: https://www.hackerrank.com/challenges/mark-and-toys/problem
#  Score: 35


n, k = map(int, input().split())
prices = s..(l..(map(int, input().split())))

count = 0
total_sum = 0
___ i __ prices:
    total_sum += i
    __ total_sum > k:
        break
    ____:
        count += 1
print(count)
