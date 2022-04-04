# Problem: https://www.hackerrank.com/challenges/triple-sum/problem
#  Score: 40


___ binary_search_last(arr, el, low, high
    __ low + 1 >_ high:
        __ arr[low] > el:
            r.. 0
        ____
            r.. low + 1
    middle = (low + high) // 2
    __ arr[middle] > el:
        r.. binary_search_last(arr, el, low, middle)
    ____
        r.. binary_search_last(arr, el, middle, high)


len_a, len_b, len_c = map(i.., input().s..
a = s..(s.. m..(i.., input().s..())))
b = s..(l..(s.. m..(i.., input().s..()))))
c = s..(l..(s.. m..(i.., input().s..()))))

ans = 0
___ i __ s..(b
    ans += binary_search_last(a, i, 0, l..(a * binary_search_last(c, i, 0, l..(c
print(ans)
