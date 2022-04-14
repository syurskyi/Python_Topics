'''
Created on Sep 5, 2017

@author: MT
'''
c_ Solution(o..
    ___ findRestaurant  list1, list2
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        hashmap1    # dict
        hashmap2    # dict
        ___ i, s __ e..(list1
            __ s n.. __ hashmap1:
                hashmap1[s] i
        ___ i, s __ e..(list2
            __ s n.. __ hashmap2:
                hashmap2[s] i
        minInd f__('inf')
        res    # list
        ___ s, i __ hashmap1.i..
            __ s __ hashmap2:
                ind i+hashmap2[s]
                __ ind __ minInd:
                    res.a..(s)
                ____ ind < minInd:
                    minInd ind
                    res [s]
        r.. res
    
    ___ test
        testCases [
            [
                ["Shogun", "Tapioca Express", "Burger King", "KFC"],
                ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"],
            ],
            [
                ["Shogun", "Tapioca Express", "Burger King", "KFC"],
                ["KFC", "Shogun", "Burger King"],
            ],
        ]
        ___ list1, list2 __ testCases:
            print('list1: %s' % list1)
            print('list2: %s' % list2)
            result findRestaurant(list1, list2)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
