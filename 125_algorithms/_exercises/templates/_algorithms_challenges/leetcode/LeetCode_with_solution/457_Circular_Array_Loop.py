c_ Solution:
    ___ circularArrayLoop  nums: List[i..])    b..
        ___ i __ r.. l.. nums)):
            __ nums[i] __ 0:
                c_
            
            # if slow and fast pointers collide, then there exists a loop
            slow = i
            fast = index(nums, slow)
            w.. nums[slow] * nums[fast] > 0 a.. nums[slow] * nums[index(nums, fast)] > 0:
                __ slow __ fast a.. fast != index(nums, fast
                    r_ T..
                ____ slow __ fast a.. fast __ index(nums, fast
                    ______
                slow = index(nums, slow)
                fast = index(nums, index(nums, fast))
                
            # set path to all 0s since it doesn't work
            runner = i
            value = nums[runner]
            w.. nums[runner] * value > 0:
                temp = index(nums, runner)
                nums[runner] = 0
                runner = temp
        r_ F..
            
    ___ index  nums, index
        length = l.. nums)
        r_ (index + nums[index] + length) % length
