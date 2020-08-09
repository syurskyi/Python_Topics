amount_values = int(input())
results = []

___ get_sorting_indexes(array
    sorted_array = array.copy()
    n = le.(array)
    ___ i in range(n
        ___ j in range(n-i-1
            __(sorted_array[j] > sorted_array[j+1]
                sorted_array[j], sorted_array[j+1] = sorted_array[j+1], sorted_array[j]

    print(array)

    ___ i in sorted_array:
        results.append(array.index(i)+1)

array = list(map(int, input().split()))
get_sorting_indexes(array)

print(*results)
