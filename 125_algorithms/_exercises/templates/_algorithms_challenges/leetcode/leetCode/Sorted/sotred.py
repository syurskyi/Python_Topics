# 各种排序。
import random

test_list = (
    list r..(10)),
    list r..(100)),
    list r..(1000)),
    list r..(10001)),
    list r..(50000))
)

list(map(random.shuffle, test_list))

result = (
    list r..(10)),
    list r..(100)),
    list r..(1000)),
    list r..(10001)),
    list r..(50000))
)

# 选择排序:
# 每次选取一个最小的值。


___ selectionSort(shuffledList

    new   # list
    ___ i __ r..(l..(shuffledList)):
        currentMinValue = min(shuffledList)
        new.append(currentMinValue)
        shuffledList.remove(currentMinValue)

    r_ new

# 插入排序。
# 例：
# 插入排序一次只换一格。
# 4， 2， 3， 5， 9， 6， 1
# 2， 4， 3， 5， 9， 6， 1

# def  insertingSort(shuffledList):
    
#     new = shuffledList.copy()

#     length = len(new)
        
#     for i in range(1, length):
#         if new[i] < new[i-1]:
#             new[i], new[i-1] = new[i-1], new[i]

#     return new
# def insertingSort(lst):
#         for i  in range(1,len(lst)):
#                 j = 0
#                 while lst[i] > lst[j]:
#                         j += 1
#                 results = lst[i]
#                 lst.pop(i)
#                 lst.insert(j,results)
#         return lst

# 归并排序
# 归并排序是将一个大问题分解成多个小问题来解决。
# 归并排序包含两个步骤，其一是分解，其二是合并。
# 在排序中分解的过程就是将一整个数组分解为多个小数组。
# 合并则是两两合并，每次都分别从一个数组中提取一个进行比较，将较小的放入新的数组中。


___ combined(list1, list2
        new   # list        
        indexOne = 0
        indexTwo = 0
        lengthOne, lengthTwo = l..(list1), l..(list2)
        _____ indexOne < lengthOne and indexTwo < lengthTwo:
            valueOne = list1[indexOne]
            valueTwo = list2[indexTwo]

            __ valueOne > valueTwo:
                new.append(valueTwo)
                indexTwo += 1
            ____
                new.append(valueOne)
                indexOne +=1

        __ indexOne __ lengthOne:
            new.e..(list2[indexTwo:])
            r_ new

        __ indexTwo __ lengthTwo:
            new.e..(list1[indexOne:])
            r_ new


___ makeValueInList(value
    r_ [value]


___ reduce(splitedList
    length = l..(splitedList)
    __ length __ 1:
        r_ splitedList[0]

    middle = length // 2
    left = reduce(splitedList[:middle])
    right = reduce(splitedList[middle:])

    r_ combined(left, right)


___ mergeSort(shuffledList

    splitedList = list(map(makeValueInList, shuffledList)) 

    result = reduce(splitedList)

    r_ result


# 快速排序
# 快速排序的思路与归并排序一样都是基于分治，将一个大问题变成小问题再组合起来。
# 快排的平均时间消耗是O(logn), 当然最差也有n²。
# 快排的思路是，选取一个元素，将大于它的放在左边，小于的放在右边。然后将左边右边再次进行相同的操作。

___ fastSort(shuffledList
    __ l..(shuffledList) <= 1:
        r_ shuffledList

    right = [i ___ i __ shuffledList[1:] __ i < shuffledList[0]]
    left = [i ___ i __ shuffledList[1:] __ i >= shuffledList[0]]

    r_ fastSort(right) + [shuffledList[0]] + fastSort(left)


___ i, j __ zip(test_list, result
    assert fastSort(i) __ j
    # assert mergeSort(i) == j
    # break
    # assert insertingSort(i) == j
    # assert selectionSort(i) == j
    # assert sorted(i) == j