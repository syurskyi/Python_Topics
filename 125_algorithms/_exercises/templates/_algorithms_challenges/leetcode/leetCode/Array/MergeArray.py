"""
好像是今日头条2018 秋招算法题？

有m名编辑审核文章，每个编辑独立工作，会把觉得有错误的地方通过下标标注出来：

[1, 10] 表示1-10个字符应该有问题。
现在要把多名编辑的结果合并起来：

[1, 10] [32, 45],
[5, 16] [78, 94]

那么合并后是 [1, 16] [32, 45] [78, 94]。

bug free.

Leetcode 中也有两个一样的：
https://leetcode.com/problems/merge-intervals/description/

测试通过：
beat 64%~95%...

这个更加类似:
https://leetcode.com/problems/insert-interval/description/

这个代码看 InsertInterval.py
"""

c.. Solution o..
    ___ merge  _sentences
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        _sentences = s..(_sentences, k.._l... x: x.start)

        __ n.. _sentences:
            r_ []

        result   # list

        head = _sentences[0].start
        tail = _sentences[0].end
        length = l..(_sentences)
        ___ x __ r..(1, length
            i = _sentences[x]
            __ tail >= i.start:
                tail = m..(tail, i.end)
            ____
                result.a.. [head, tail])
                head = i.start
                tail = i.end

        result.a.. [head, tail])
        r_ result

test = (
    [(1, 10), (32, 45)],
    [(78, 94), (5, 16)],
    [(80, 100), (200, 220), (16, 32)]
    )


___ mergeArray(sentences

    """
        这个测试数据的结构是我自己写的，所以第一步是打散数组。
        1. 根据第一个字符出现的位置进行排序。
        2. 迭代，记录i的头，记录i的末尾，末尾与下一个i的头做比较，若前者记录的大或相等则末尾替换为两者中较大的一个。
        3. 不大的情况添加到结果中，并将头尾替换为此时的数据。
        4. 最后一轮迭代在添加一次。

    """

    # 打散，相当于原题给的数据中的读入。
    _sentences = s..([y ___ x __ test ___ y __ x], k.._l... x: x[0])

    __ n.. _sentences:
        r_ []

    result   # list

    head = _sentences[0][0]
    tail = _sentences[0][1]
    length = l..(_sentences)
    ___ x __ r..(1, length
        i = _sentences[x]
        __ tail >= i[0]:
            tail = m..(tail, i[1])
        ____
            result.a.. [head, tail])
            head = i[0]
            tail = i[1]

    result.a.. [head, tail])
    print(result)

mergeArray(test)

