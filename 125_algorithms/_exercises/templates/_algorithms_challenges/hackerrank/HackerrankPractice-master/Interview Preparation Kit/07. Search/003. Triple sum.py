# Problem: https://www.hackerrank.com/challenges/triple-sum/problem
#  Score: 40


___ binary_search_last(arr, el, low, high
    __ low + 1 >= high:
        __ arr[low] > el:
            r_ 0
        ____
            r_ low + 1
    middle = (low + high) // 2
    __ arr[middle] > el:
        r_ binary_search_last(arr, el, low, middle)
    ____
        r_ binary_search_last(arr, el, middle, high)


len_a, len_b, len_c = map(int, input().split())
a = sorted(set(map(int, input().split())))
b = sorted(list(set(map(int, input().split()))))
c = sorted(list(set(map(int, input().split()))))

ans = 0
___ i in set(b
    ans += binary_search_last(a, i, 0, le.(a)) * binary_search_last(c, i, 0, le.(c))
print(ans)
