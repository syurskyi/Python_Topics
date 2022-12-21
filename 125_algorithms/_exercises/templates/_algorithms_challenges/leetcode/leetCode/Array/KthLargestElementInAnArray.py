"""
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note: 
You may assume k is always valid, 1 ≤ k ≤ array's length.

返回第 k 大个数，与 Third maximum numbers 思路一致：
找到第 k 大个数一般的思路有：
1. 排序后放到数组中，排序算法使用归并和快排在理想情况下都是O(nlogn)，归并比较稳定一些。之后的索引是O(1)。
   这种的适合并不需要插入的情况，因为每次插入的时间复杂度为 O(n)。

2. 建立二叉搜索树，进阶的话红黑树或AVL树。
   这种情况下搜索和插入在理想情况下都是O(logn)。

由于不会有插入，所以选用排序。

测试用例：
https://leetcode.com/problems/kth-largest-element-in-an-array/description/

内置排序beat 99%，重新写一下归并和快排比比试试。
自己写的归并排序，beat 40% .
快速排序由于基准点问题第一次直接 TLE.
好吧，修改一下，选取基准点的方法基本是：
1. 取左端或右端。
2. 随机取。
3. 取左右中三者中中间的一个。
三者取中间的一个直接用了排序，做了个对比：
内置的sorted在用key的时候是最快的，自己的merge sort 用 key 会比较慢。
差距很明显，如果用的内置sorted，时间基本与merge sort一致，若用的merge sort，时间慢了100倍。

多次测试后：
内置 < merge sort < quick sort.
merge sort 和 quick sort 差距较小。

"""
c.. Solution o..

    ___ quickSort  unsorted_list
        """
            每次都选一个基准点，大的放在右边，小的放在左边，等于的随便归到一个地方，不断拆分拆分。
            这里直接选用[0]，当然这种情况下往往会发生不理想的情况，
            不理想的情况表示每次恰好都是最小或最大，这样的结果会直接导致算法变为O(n^2).
        """

        __ l..(unsorted_list) <= 1:
            r_ unsorted_list

        left   # list
        right   # list

        meta = self._getMiddle(unsorted_list)
        ___ i __ unsorted_list[:meta] + unsorted_list[meta+1:]:
            __ i <= unsorted_list[meta]:
                left.append(i)
                c_
            right.append(i)

        r_ self.quickSort(left) + [unsorted_list[meta]] + self.quickSort(right)

    ___ _getMiddle  unsorted_list
        """
            返回快排所需的基准点，
            左右中中间选择一个。
            若不足3位，选左。
        """
        __ l..(unsorted_list) < 3:
            r_ 0

        left = unsorted_list[0]
        right = unsorted_list[-1]
        middle = unsorted_list[l..(unsorted_list) // 2]
        l, r, m = [(0, left), (l..(unsorted_list) - 1, right), (l..(unsorted_list) // 2, middle)]
        # 这里对比了自己写的merge sort 与内置的差距，
        # 在有key的情况下差距非常大。
        r_ s..([l, r, m], k.._l... x: x[1])[1][0]


    ___ mergeSort  unsorted_list, key=None
        """
            归并排序的基本思路是分治，把一个大问题分解成小问题。逐个解决小问题。
            以长度的一半为基准点，将一个大列表分为两个小列表，一直分一直分，然后合并。
            所以排序分为两步：
               第一步是分解，第二步是合并。
        """
        __ l..(unsorted_list) <= 1:
            r_ unsorted_list

        break_point = l..(unsorted_list) // 2

        left = self.mergeSort(unsorted_list[:break_point])
        right = self.mergeSort(unsorted_list[break_point:])

        r_ self._decomposeAndMerge(left, right, key=key)

    ___ _decomposeAndMerge  unsorted_list_A, unsorted_list_B, key
        sorted_list   # list
        a = 0
        b = 0
        length_A = l..(unsorted_list_A)
        length_B = l..(unsorted_list_B)
        _____ a < length_A a.. b < length_B:

            __ unsorted_list_A[a] <= unsorted_list_B[b]:
                sorted_list.append(unsorted_list_A[a])
                a += 1
            ____
                sorted_list.append(unsorted_list_B[b])
                b += 1            
        __ a < length_A:
            sorted_list.e..(unsorted_list_A[a:])
        ____
            sorted_list.e..(unsorted_list_B[b:])

        r_ sorted_list


    ___ findKthLargest  nums, k
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        r_ s..(nums, reverse=True)[k-1]

s = Solution()
a = list r..(50000))
print(s.quickSort(a))
# 1

