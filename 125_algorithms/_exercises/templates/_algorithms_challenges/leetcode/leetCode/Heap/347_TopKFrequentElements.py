#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com
# @Last Modified time: 2016-07-09 09:41:55


c.. Solution o..
    ___ topKFrequent  nums, k
        """ Given a non-empty array of integers, return the k most frequent elements.

        heapq.nlargest(n, iterable[, key])
        Return a list with the n largest elements from the dataset defined by iterable.
        """
        num_count = collections.Counter(nums)
        r_ heapq.nlargest(k, num_count, k.._l... x: num_count[x])


c.. Solution_2 o..
    ___ topKFrequent  nums, k
        ''' Use Counter to extract the top k frequent elements

        most_common(k) return a list of tuples,
        where the first item of the tuple is the element,
        and the second item of the tuple is the count
        Thus, the built-in zip function could be used to extract
        the first item from the tuples
        '''
        r_ zip(*collections.Counter(nums).most_common(k))[0]

"""
[1,1,1,2,2,3]
2
[1,1,2,3,3,3,4,4,4,4,1,1,1]
3
"""
