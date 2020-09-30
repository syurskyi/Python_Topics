
class Solution(object
    ___ numberOfArithmeticSlices(self, A
        nums = A
        n = le.(nums)
        res = 0
        dp = [{} ___ _ __ range(n)]
        ___ i __ range(n
            num1 = nums[i]
            ___ j __ range(i
                num2 = nums[j]
                diff = num2-num1
                c1 = dp[i].get(diff, 0)
                c2 = dp[j].get(diff, 0)
                res += c2
                dp[i][diff] = c1+c2+1
        r_ res
    
    ___ test(self
        testCases = [
            [2, 4, 6, 8, 10],
        ]
        ___ nums __ testCases:
            print('nums: %s' % nums)
            result = self.numberOfArithmeticSlices(nums)
            print('result: %s' % result)
            print('-='*30+'-')

__  -n __ '__main__':
    Solution().test()
