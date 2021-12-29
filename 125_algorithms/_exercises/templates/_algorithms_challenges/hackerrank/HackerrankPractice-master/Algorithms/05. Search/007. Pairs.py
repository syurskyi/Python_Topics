# Problem: https://www.hackerrank.com/challenges/pairs/problem
# Score: 50


# use two-pointers approach on a sorted array
n, value = map(int, input().split())
points = s..(l..(map(int, input().split())))

ans = 0
i = 0
j = 1

while j < n:
    __ points[j] - points[i] __ value:
        ans += 1
        j += 1
    ____ points[j] - points[i] > value:
        i += 1
    ____ points[j] - points[i] < value:
        j += 1

print(ans)
