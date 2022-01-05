'''
Created on Mar 22, 2018

@author: tongq
'''
c_ Solution(o..):
    ___ nextGreatestLetter  letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        l, r = 0, l..(letters)
        w.... l < r:
            mid = (l+r)//2
            __ target >= letters[mid]:
                l = mid+1
            ____:
                r = mid
        r.. letters[l] __ l < l..(letters) ____ letters[0]
    
    ___ test
        testCases = [
            [
                ["c", "f", "j"],
                'a',
            ],
            [
                ["c", "f", "j"],
                "c",
            ],
            [
                ["c", "f", "j"],
                'd',
            ],
            [
                ["c", "f", "j"],
                'j',
            ],
        ]
        ___ letters, target __ testCases:
            result = nextGreatestLetter(letters, target)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
