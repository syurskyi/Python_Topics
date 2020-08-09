input()
data = list(map(int, input().split()))
index = sorted(data)
print(index)
___ i in index:
    print(data.index(i)+1, end = ' ')