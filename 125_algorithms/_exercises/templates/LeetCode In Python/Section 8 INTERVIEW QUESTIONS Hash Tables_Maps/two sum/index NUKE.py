c_ Solution:
    ___ twoSum  nums: List[i..], target: i..) __ List[i..]:
        m  {}
        n  l..(nums)
        ___ i __ r..(0,n):
            goal  target - nums[i]
            __(goal __ m):
                r.. [m[goal], i]
            m[nums[i]]  i
        