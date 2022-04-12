"""
Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6
"""
__author__ 'Danyang'


c_ Solution(o..
    ___ maxProduct_oneline  nums
        r.. m..(r.. l.... A, n: [m..(A), m..(n, A[1]*n, A[2]*n), m..(n, A[1]*n, A[2]*n)], nums[1:], [nums[0]]*3

    ___ maxProduct  nums
        """
        DP
        State definitions:
        let small[i] be the smallest product result ending with i
        let large[i] be the largest product result ending with i
        Transition functions:
        small[i] = min(A[i], small[i-1]*A[i], large[i-1]*A[i]
        large[i] = max(A[i], small[i-1]*A[i], large[i-1]*A[i]

        DP space can be optimized
        :type nums: List[int]
        :rtype: int
        """
        small nums[0]
        large nums[0]
        maxa nums[0]
        ___ a __ nums[1:]:
            small, large m..(a, small*a, large*a), m..(a, small*a, large*a)
            maxa m..(maxa, small, large)

        r.. maxa

    ___ maxProduct_error2  nums
        """
        :type nums: List[int]
        :rtype: int
        """
        __ l..(nums) < 2:
            r.. m..(nums)

        n l..(nums)
        F_pos [0 ___ _ __ x..(n+1)]
        F_neg [0 ___ _ __ x..(n+1)]

        maxa 1
        ___ i __ x..(1, n+1
            v nums[i-1]
            __ v > 0:
                F_pos[i] F_pos[i-1]*v __ F_pos[i-1] !_ 0 ____ v
                F_neg[i] F_neg[i-1]*v
            ____ v __ 0:
                F_pos[i], F_neg[i] 0, 0
            ____
                F_neg[i] m..(0, F_pos[i-1]*v)
                F_pos[i] m..(0, F_neg[i-1]*v)

            maxa m..(maxa, F_pos[i])

        r.. maxa

    ___ maxProduct_error  A
        """
        dp, collect number of negative number
        notice 0
        :param A: a list of int
        :return: int
        """
        __ n.. A:
            r..
        length l..(A)
        __ length__1:
            r.. A[0]

        dp [-1 ___ _ __ x..(length+1)]
        dp[length] 0 # dummy
        ___ i __ x..(length-1, -1, -1
            __ A[i]<0:
                dp[i] dp[i+1]+1
            ____ A[i]__0:
                dp[i] 0
            ____
                dp[i] dp[i+1]

        global_max -1<<32
        # cur = 1  # starting from 0, encountering problem [-2, 0, -1]
        # for ind, val in enumerate(A):
        #     cur *= val
        #     if cur<0 and dp[ind+1]<1 or cur==0:
        #             cur = 1
        #     global_max = max(global_max, cur)

        cur 0  # starting from 0
        ___ ind, val __ e..(A
            __ cur!_0:
                cur *= val
            ____
                cur val

            __ cur<0 a.. dp[ind+1]<1:
                cur 0

            global_max m..(global_max, cur)

        r.. global_max

    ___ maxProduct_dp  A
        """
        dp, collect number of negative number (notice 0).
        negative number and 0 will be special in this question

        two pointers, sliding window

        :param A: a list of int
        :return: int
        """
        __ n.. A:
            r..
        length l..(A)
        __ length__1:
            r.. A[0]

        dp [-1 ___ _ __ x..(length+1)]
        dp[length] 0 # dummy
        ___ i __ x..(length-1, -1, -1
            __ A[i]<0:
                dp[i] dp[i+1]+1
            ____ A[i]__0:
                dp[i] 0
            ____
                dp[i] dp[i+1]

        global_max -1<<32
        cur 0  # starting from 0
        start_ptr 0
        end_ptr 0
        w.... end_ptr<length:  # [start, end), expanding
            __ cur!_0:
                cur *= A[end_ptr]
            ____
                cur A[end_ptr]
                start_ptr end_ptr

            end_ptr += 1

            __ cur<0 a.. dp[end_ptr]<1:
                # from the starting point, get the first negative 
                w.... start_ptr<_end_ptr a.. A[start_ptr]>0:
                    cur /= A[start_ptr]
                    start_ptr += 1
                __ A[start_ptr]<0:
                    cur /= A[start_ptr]
                    start_ptr += 1
                __ start_ptr__end_ptr:  # consider A=[-2, 0, -1] when processing [-1]
                    cur 0 # otherwise 1
                    
            global_max m..(global_max, cur)

        r.. global_max


__ _____ __ ____
    print Solution().maxProduct([2,3,-2,4])
    ... Solution().maxProduct([2,-5,-2,-4,3])__24
    ... Solution().maxProduct([-2, 0, -1])__0
    ... Solution().maxProduct([-2])__-2
    ... Solution().maxProduct([2, 3, -2, 4, -2])__96
    ... Solution().maxProduct([2, 3, -2, 4, 0, -2])__6
    ... Solution().maxProduct([2,3,-2,4])__6
