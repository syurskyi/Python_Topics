#! /usr/bin/env python
# -*- coding: utf-8 -*-


c.. Solution o..
    # Easy to understand: recursively.
    # Just like get permute for distinct numbers.
    ___ permuteUnique  nums
        ans   # list
        nums.s.. )
        self.dfs(nums, 0, ans)
        r_ ans

    ___ dfs  num, begin, ans
        __ begin __ l..(num) - 1:
            ans.a.. num)
            r_

        ___ i __ r..(begin, l..(num)):
            __ i != begin a.. num[i] __ num[begin]:
                c_
            num[i], num[begin] = num[begin], num[i]
            # num[:], get a new copy.  Just like pass by value
            self.dfs(num[:], begin + 1, ans)


c.. Solution_2 o..
    '''
    1. sort nums in ascending order, add it to res;
    2. generate the next permutation of nums, and add it to res;
    3. repeat 2 until the next permutation of nums.
    '''
    ___ permuteUnique  nums
        nums.s.. )
        ans   # list
        ans.a.. nums[:])
        _____ self.nextPermutation(nums
            ans.a.. nums[:])

        r_ ans

    ___ nextPermutation  nums
        length = l..(nums)
        index = length - 1

        _____ index >= 1:
            __ nums[index] > nums[index - 1]:
                ___ i __ r..(length - 1, index - 1, -1
                    __ nums[i] > nums[index - 1]:
                        nums[i], nums[index - 1] = nums[index - 1], nums[i]
                        nums[index:] = s..(nums[index:])
                        r_ True
            ____
                index -= 1

        # Nums is in descending order, just reverse it.
        r_ False


"""
[]
[1]
[1,2,3]
[2,2,3,3]
"""
