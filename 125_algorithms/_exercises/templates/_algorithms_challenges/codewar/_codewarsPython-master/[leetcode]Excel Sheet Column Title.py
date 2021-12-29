class Solution:
    # @param {integer} n
    # @return {string}
    ___ convertToTitle(self, n):
        times = 0
        res = []
        while n >= 27:
            res.append(n % 27)
            n %= 27
            times += 1
            __ times == 10000:
                break
        res.append(n)
        return res

test = Solution()
for i in range(24,30):
    print(test.convertToTitle(i))