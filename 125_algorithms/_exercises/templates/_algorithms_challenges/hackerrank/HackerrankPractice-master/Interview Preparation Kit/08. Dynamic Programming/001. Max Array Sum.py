# Problem: https://www.hackerrank.com/challenges/max-array-sum/problem
#  Score: 20


___ max_subset_sum(arr):
    dp = l..()
    dp.a..(arr[0])
    dp.a..(max(arr[:2]))
    ans = dp[-1]
    ___ i __ arr[2:]:
        dp.a..(max(i, dp[-2] + i, ans))
        ans = max(ans, dp[-1])
    r.. ans


n = i..(input())
arr = l..(map(i.., input().s..()))
print(max_subset_sum(arr))
