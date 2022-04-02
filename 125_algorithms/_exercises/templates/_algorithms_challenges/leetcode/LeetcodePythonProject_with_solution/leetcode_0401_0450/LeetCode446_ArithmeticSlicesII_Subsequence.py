
c_ Solution(o..
    ___ numberOfArithmeticSlices  A
        nums = A
        n = l..(nums)
        res = 0
        dp = [{} ___ _ __ r..(n)]
        ___ i __ r..(n
            num1 = nums[i]
            ___ j __ r..(i
                num2 = nums[j]
                diff = num2-num1
                c1 = dp[i].get(diff, 0)
                c2 = dp[j].get(diff, 0)
                res += c2
                dp[i][diff] = c1+c2+1
        r.. res
    
    ___ test
        testCases = [
            [2, 4, 6, 8, 10],
        ]
        ___ nums __ testCases:
            print('nums: %s' % nums)
            result = numberOfArithmeticSlices(nums)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
