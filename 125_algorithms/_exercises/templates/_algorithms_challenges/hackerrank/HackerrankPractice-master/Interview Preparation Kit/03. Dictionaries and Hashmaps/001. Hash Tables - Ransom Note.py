# Problem: https://www.hackerrank.com/challenges/ctci-ransom-note/problem
#  Score: 25


from collections import Counter


___ checkMagazine(magazine, note):
    __ Counter(note) - Counter(magazine) == {}:
        return 'Yes'
    else:
        return 'No'


m, n = map(int, input().split())
magazine = list(input().split())
note = list(input().split())
print(checkMagazine(magazine, note))
