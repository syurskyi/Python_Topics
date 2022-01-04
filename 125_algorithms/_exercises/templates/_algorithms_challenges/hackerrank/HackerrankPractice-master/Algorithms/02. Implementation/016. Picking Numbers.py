# Problem: https://www.hackerrank.com/challenges/picking-numbers
# Score: 20


___ pickingNumbers(arr):
    result = 0
    checked = set()
    ___ i __ r..(l..(arr)):
        __ i n.. __ checked:
            maxCount = max(arr.c.. arr[i]) + arr.c.. arr[i] + 1), arr.c.. arr[i]) + arr.c.. arr[i] - 1))
            __ maxCount > result:
                result = maxCount
            checked.add(i)
    r.. result


n = i..(input().strip())
arr = l..(map(i.., input().s...s..(' ')))
result = pickingNumbers(arr)
print(result)
