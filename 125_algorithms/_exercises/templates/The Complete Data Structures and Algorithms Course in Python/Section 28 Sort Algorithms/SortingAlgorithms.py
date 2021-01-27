#   Created by Elshad Karimov 
#   Copyright © 2021 AppMillers. All rights reserved.

import math

___ bubbleSort(customList
    ___ i __ range(le_(customList)-1
        ___ j __ range(le_(customList)-i-1
            __ customList[j] > customList[j+1]:
                customList[j], customList[j+1] = customList[j+1], customList[j]
    print(customList)


___ selectionSort(customList
    ___ i __ range(le_(customList)):
        min_index = i
        ___ j __ range(i+1, le_(customList)):
            __ customList[min_index] > customList[j]:
                min_index = j
        customList[i], customList[min_index] = customList[min_index], customList[i]
    print(customList)

___ insertionSort(customList
    ___ i __ range(1, le_(customList)):
        key = customList[i]
        j = i-1
        w__ j>=0 and key < customList[j]:
            customList[j+1] = customList[j]
            j -= 1
        customList[j+1] = key
    r_ customList


___ bucketSort(customList
    numberofBuckets = round(math.sqrt(le_(customList)))
    maxValue = max(customList)
    arr = []

    ___ i __ range(numberofBuckets
        arr.ap..([])
    ___ j __ customList:
        index_b = math.ceil(j*numberofBuckets/maxValue)
        arr[index_b-1].ap..(j)
    
    ___ i __ range(numberofBuckets
        arr[i] = insertionSort(arr[i])
    
    k = 0
    ___ i __ range(numberofBuckets
        ___ j __ range(le_(arr[i])):
            customList[k] = arr[i][j]
            k += 1
    r_ customList

___ merge(customList, l, m, r
    n1 = m - l + 1
    n2 = r - m

    L = [0] * (n1)
    R = [0] * (n2)

    ___ i __ range(0, n1
        L[i] = customList[l+i]
    
    ___ j __ range(0, n2
        R[j] = customList[m+1+j]
    
    i = 0 
    j = 0
    k = l
    w__ i < n1 and j < n2:
        __ L[i] <= R[j]:
            customList[k] = L[i]
            i += 1
        ____
            customList[k] = R[j]
            j += 1
        k += 1
    w__ i < n1:
        customList[k] = L[i]
        i += 1
        k += 1
    
    w__ j < n2:
        customList[k] = R[j]
        j += 1
        k += 1

___ mergeSort(customList, l, r
    __ l < r:
        m = (l+(r-1))//2
        mergeSort(customList, l, m)
        mergeSort(customList, m+1, r)
        merge(customList, l, m, r)
    r_ customList

___ partition(customList, low, high
    i = low - 1
    pivot = customList[high]
    ___ j __ range(low,high
        __ customList[j] <= pivot:
            i += 1
            customList[i], customList[j] = customList[j], customList[i]
    customList[i+1], customList[high] = customList[high], customList[i+1]
    r_ (i+1)

___ quickSort(customList, low, high
    __ low < high:
        pi = partition(customList, low, high)
        quickSort(customList, low, pi-1)
        quickSort(customList, pi+1, high)


___ heapify(customList, n, i
    smallest = i
    l = 2*i + 1
    r = 2*i + 2
    __ l < n and customList[l] < customList[smallest]:
        smallest = l
    
    __ r < n and customList[r] < customList[smallest]:
        smallest = r
    
    __ smallest != i:
        customList[i], customList[smallest] = customList[smallest], customList[i]
        heapify(customList, n, smallest)


___ heapSort(customList
    n = le_(customList)
    ___ i __ range(int(n/2)-1, -1, -1
        heapify(customList, n, i)
    
    ___ i __ range(n-1,0,-1
        customList[i], customList[0] = customList[0], customList[i]
        heapify(customList, i, 0)
    # customList.reverse()



cList = [2,1,7,6,5,3,4,9,8]
heapSort(cList)
print(cList)




        