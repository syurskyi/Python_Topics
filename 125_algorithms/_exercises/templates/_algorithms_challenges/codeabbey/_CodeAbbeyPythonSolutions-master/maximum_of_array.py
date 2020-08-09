values = list(map(int, input().split()))

___ get_max_and_min(
    max = values[0]
    min = values[0]
    ___ i in values:
        __(i < min
            min = i
        ____(i > max
            max = i
    
    r_ max, min

max, min = get_max_and_min()

print(max, min)