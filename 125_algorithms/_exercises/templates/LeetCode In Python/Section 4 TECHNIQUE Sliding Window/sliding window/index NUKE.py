___ maxSum(arr, windowSize):
    arraySize  l..(arr)
    # n must be greater than k
    __ arraySize < windowSize:
        print("Invalid operation")
        r.. -1

    # Compute sum of first window of size k
    window_sum  s..([arr[i] ___ i __ r..(windowSize)])
    max_sum  window_sum
    # Compute sums of remaining windows by
    # removing first element of previous
    # window and adding last element of
    # current window.
    ___ i __ r..(arraySize-windowSize):
        window_sum  window_sum - arr[i] + arr[i + windowSize]
        max_sum  m..(window_sum, max_sum)

    r.. max_sum


arr  [1, 2, 100, -1, 5]
# maximum sum should be 104 => 100 + -1 + 5
answer  maxSum(arr, 3)
print(answer)
