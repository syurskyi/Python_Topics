___ max_sum_subarray(arr
    global_max = arr[0]
    local_max = arr[0]
    ___ i __ ra__(1, le_(arr)):
        local_max = ma_(local_max + arr[i], arr[i])
        global_max = ma_(global_max, local_max)
    r_ global_max


arr = [-2, -1, 3, -2, 4, 3, -3, 5]
max_sum = max_sum_subarray(arr)
print(max_sum)
