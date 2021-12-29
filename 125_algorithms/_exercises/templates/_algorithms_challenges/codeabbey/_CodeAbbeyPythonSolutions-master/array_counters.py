M, N = map(int, input().split())

results = [0]*N

___ count(array):
    for i in array:
        results[i-1] += 1

array = list(map(int, input().split()))
count(array)
print(*results)