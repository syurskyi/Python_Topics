# Problem: https://www.hackerrank.com/challenges/ctci-ice-cream-parlor/problem
#  Score: 35


t = int(input())
___ i __ range(t
    money = int(input())
    n = int(input())
    arr = list(map(int, input().split()))

    saved_values = {}
    ___ counter, value __ enumerate(arr
        __ money-value __ saved_values:
            print(saved_values[money-value] + 1, counter + 1)
        ____ value not __ saved_values:
            saved_values[value] = counter
