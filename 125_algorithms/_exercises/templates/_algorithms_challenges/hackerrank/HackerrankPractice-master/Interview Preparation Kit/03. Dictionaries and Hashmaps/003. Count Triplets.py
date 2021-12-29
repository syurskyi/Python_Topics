# Problem: https://www.hackerrank.com/challenges/count-triplets-1/problem
#  Score: 25


____ collections _______ defaultdict


___ count_triplets(arr, r):
    arr2 = defaultdict(int)
    arr3 = defaultdict(int)
    count = 0
    ___ i __ arr:
        count += arr3[i]
        arr3[i*r] += arr2[i]
        arr2[i*r] += 1
    r.. count


n, r = map(int, input().s..())
arr = l..(map(int, input().s..()))
print(count_triplets(arr, r))
