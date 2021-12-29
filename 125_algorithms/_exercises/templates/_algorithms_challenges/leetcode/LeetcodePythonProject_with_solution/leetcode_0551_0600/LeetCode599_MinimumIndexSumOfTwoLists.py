'''
Created on Sep 5, 2017

@author: MT
'''
class Solution(object):
    ___ findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        hashmap1 = {}
        hashmap2 = {}
        ___ i, s __ enumerate(list1):
            __ s n.. __ hashmap1:
                hashmap1[s] = i
        ___ i, s __ enumerate(list2):
            __ s n.. __ hashmap2:
                hashmap2[s] = i
        minInd = float('inf')
        res    # list
        ___ s, i __ hashmap1.items():
            __ s __ hashmap2:
                ind = i+hashmap2[s]
                __ ind __ minInd:
                    res.a..(s)
                ____ ind < minInd:
                    minInd = ind
                    res = [s]
        r.. res
    
    ___ test(self):
        testCases = [
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
            result = self.findRestaurant(list1, list2)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
