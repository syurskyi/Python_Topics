c_ Solution(object):
    ___ totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        left = 0
        res = 0
        hashmap    # dict
        ___ i, num __ e..(tree):
            hashmap[num] = hashmap.get(num, 0) + 1
            w.... l..(hashmap) > 2:
                hashmap[tree[left]] -= 1
                __ hashmap[tree[left]] __ 0:
                    del hashmap[tree[left]]
                left += 1
            res = max(res, i-left+1)
        res = max(res, l..(tree)-left)
        r.. res

    ___ test
        testCases = [
            [0,1,2],
            [1,2,1],
            [0,1,2,2],
            [1,2,3,2,2],
            [3,3,3,1,2,1,1,2,3,3,4],
        ]
        ___ tree __ testCases:
            res = totalFruit(tree)
            print('res: %s' % res)
            print('-='*30+'-')


__ __name__ __ '__main__':
    Solution().test()
