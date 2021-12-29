
class Solution(object):
    ___ wiggleSort(self, nums):
        median = self.kthLargestElement(nums, (l..(nums)+1)//2)
        n = l..(nums)
        left = 0
        i = 0
        right = n-1
        while i <= right:
            __ nums[self.newIndex(i, n)] > median:
                nums[self.newIndex(left, n)], nums[self.newIndex(i, n)] =\
                nums[self.newIndex(i, n)], nums[self.newIndex(left, n)]
                left += 1
                i += 1
            ____ nums[self.newIndex(i, n)] < median:
                nums[self.newIndex(right, n)], nums[self.newIndex(i, n)] =\
                nums[self.newIndex(i, n)], nums[self.newIndex(right, n)]
                right -= 1
            ____:
                i += 1
    
    ___ newIndex(self, index, n):
        r.. (1+2*index)%(n|1)
    
    ___ kthLargestElement(self, nums, k):
        self.shuffle(nums)
        lo = 0
        hi = l..(nums)-1
        k = l..(nums)-k
        while lo < hi:
            j = self.partition(nums, lo, hi)
            __ j < k:
                lo = j+1
            ____ j > k:
                hi = j-1
            ____:
                break
        r.. nums[k]
    
    ___ partition(self, nums, lo, hi):
        i, j = lo+1, hi
        while True:
            while i < hi and nums[i] <= nums[lo]:
                i += 1
            while j > lo and nums[lo] <= nums[j]:
                j -= 1
            __ i >= j:
                break
            nums[i], nums[j] = nums[j], nums[i]
        nums[lo], nums[j] = nums[j], nums[lo]
        r.. j
    
    ___ shuffle(self, nums):
        _______ random
        ___ i __ r..(l..(nums)-1, 0, -1):
            ind = random.randint(0, i)
            nums[i], nums[ind] = nums[ind], nums[i]
    
    ___ wiggleSortWithSorting(self, nums):
        nums.sort()
        half = l..(nums[::2])-1
        nums[::2], nums[1::2] = nums[half::-1], nums[:half:-1]
    
    ___ test(self):
        testCases = [
            [1, 5, 1, 1, 6, 4],
            [1, 3, 2, 2, 3, 1],
            [1, 2, 2, 1, 2, 1, 1, 1, 1, 2, 2, 2],
        ]
        ___ nums __ testCases:
            print('nums: %s' % (nums))
            self.wiggleSort(nums)
            print('sorted: %s' % (nums))
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()
