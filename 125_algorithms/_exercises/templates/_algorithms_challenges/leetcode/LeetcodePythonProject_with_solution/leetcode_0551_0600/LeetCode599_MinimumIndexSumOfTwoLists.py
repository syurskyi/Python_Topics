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
        for i, s in enumerate(list1):
            __ s not in hashmap1:
                hashmap1[s] = i
        for i, s in enumerate(list2):
            __ s not in hashmap2:
                hashmap2[s] = i
        minInd = float('inf')
        res = []
        for s, i in hashmap1.items():
            __ s in hashmap2:
                ind = i+hashmap2[s]
                __ ind == minInd:
                    res.append(s)
                elif ind < minInd:
                    minInd = ind
                    res = [s]
        return res
    
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
        for list1, list2 in testCases:
            print('list1: %s' % list1)
            print('list2: %s' % list2)
            result = self.findRestaurant(list1, list2)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ == '__main__':
    Solution().test()
