___ find_pairs_with_given_difference(arr, k
    ans = []

    __ not arr or not isinstance(k, int
        r_ ans

    n = le.(arr)
    sums = {}

    for i in range(n
        sums[arr[i] - k] = i

    for j in range(n
        __ arr[j] in sums:
            i = sums[arr[j]]
            ans.append([arr[i], arr[j]])

    r_ ans
