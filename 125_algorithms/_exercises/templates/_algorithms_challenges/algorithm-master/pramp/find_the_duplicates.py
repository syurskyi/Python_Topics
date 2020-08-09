___ find_duplicates(arr1, arr2
    ans = []

    __ not arr1 or not arr2:
        r_ ans

    m, n = le.(arr1), le.(arr2)
    i = j = 0

    w___ i < m and j < n:
        __ arr1[i] < arr2[j]:
            i += 1
        ____ arr1[i] > arr2[j]:
            j += 1
        ____
            __ not ans or arr1[i] != ans[-1]:
                ans.append(arr1[i])
            i += 1
            j += 1

    r_ ans


___ find_duplicates2(arr1, arr2
    ans = []

    __ not arr1 or not arr2:
        r_ ans

    vals = {}

    ___ num in arr1:
        vals[num] = False

    ___ num in arr2:
        __ num in vals and vals[num] is False:
            vals[num] = True
            ans.append(num)

    r_ ans


___ find_duplicates3(arr1, arr2
    __ not arr1 or not arr2:
        r_ []

    val1 = set(arr1)
    val2 = set(arr2)

    r_ list(val1 & val2)


__ __name__ __ '__main__':
    print(find_duplicates([1, 2, 3, 5, 6, 7], [3, 6, 7, 8, 20]))
    print(find_duplicates([1, 2, 3, 3, 5, 6, 7], [3, 3, 6, 7, 8, 20]))
    print(find_duplicates2([1, 2, 3, 5, 6, 7], [3, 6, 7, 8, 20]))
    print(find_duplicates2([1, 2, 3, 3, 5, 6, 7], [3, 3, 6, 7, 8, 20]))
    print(find_duplicates3([1, 2, 3, 5, 6, 7], [3, 6, 7, 8, 20]))
    print(find_duplicates3([1, 2, 3, 3, 5, 6, 7], [3, 3, 6, 7, 8, 20]))
