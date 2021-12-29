amount_values = int(input())
results    # list

___ get_sorting_indexes(array):
    sorted_array = array.copy()
    n = l..(array)
    ___ i __ r..(n):
        ___ j __ r..(n-i-1):
            __(sorted_array[j] > sorted_array[j+1]):
                sorted_array[j], sorted_array[j+1] = sorted_array[j+1], sorted_array[j]

    print(array)

    ___ i __ sorted_array:
        results.a..(array.index(i)+1)

array = l..(map(int, input().split()))
get_sorting_indexes(array)

print(*results)
