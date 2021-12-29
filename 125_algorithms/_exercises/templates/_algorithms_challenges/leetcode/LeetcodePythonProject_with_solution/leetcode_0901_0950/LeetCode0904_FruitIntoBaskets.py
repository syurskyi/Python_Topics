class Solution(object):
    ___ totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        left = 0
        res = 0
        hashmap = {}
        for i, num in enumerate(tree):
            hashmap[num] = hashmap.get(num, 0) + 1
            while len(hashmap) > 2:
                hashmap[tree[left]] -= 1
                __ hashmap[tree[left]] == 0:
                    del hashmap[tree[left]]
                left += 1
            res = max(res, i-left+1)
        res = max(res, len(tree)-left)
        return res

    ___ test(self):
        testCases = [
            [0,1,2],
            [1,2,1],
            [0,1,2,2],
            [1,2,3,2,2],
            [3,3,3,1,2,1,1,2,3,3,4],
        ]
        for tree in testCases:
            res = self.totalFruit(tree)
            print('res: %s' % res)
            print('-='*30+'-')


__ __name__ == '__main__':
    Solution().test()
