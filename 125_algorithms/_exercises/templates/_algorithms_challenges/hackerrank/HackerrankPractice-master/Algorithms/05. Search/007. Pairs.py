# Problem: https://www.hackerrank.com/challenges/pairs/problem
# Score: 50


# use two-pointers approach on a sorted array
n, value  m.. i.., i.. ).s..
points  s..(l.. m..(i.., i.. ).s..())))

ans  0
i  0
j  1

w.... j < n:
    __ points[j] - points[i] __ value:
        ans + 1
        j + 1
    ____ points[j] - points[i] > value:
        i + 1
    ____ points[j] - points[i] < value:
        j + 1

print(ans)
