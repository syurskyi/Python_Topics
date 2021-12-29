___ merge_sort(arr, l, u
    m  0
    __ l < u:
        m  (l + u) / 2
        merge_sort(arr, l, m)
        merge_sort(arr, m + 1, u)
        merge(arr, l, m, u)

___ merge(arr, l, m, u
    n1  m - l + 1
    n2  u - m

    left  [0] * n1
    right  [0] * n2

    ___ x __ ra__(0, n1
        left[x]  arr[l + x]

    ___ y __ ra__(0, n2
        right[y]  arr[m + 1 + y]

    i  0
    j  0
    k  l

    w__ i < n1 a__ j < n2:
        __ left[i] < right[j]:
            arr[k]  left[i]
            i + 1
        ____
            arr[k]  right[j]
            j + 1
        k + 1

    w__ i < n1:
        arr[k]  left[i]
        i + 1
        k + 1

    w__ j < n2:
        arr[k]  right[j]
        j + 1
        k + 1


arr  [11, 6, 3, 9, 14, 66, 2]
n  le_(arr)

merge_sort(arr, 0, n - 1)

___ i __ ra__(n
    print ("%d" % arr[i])
