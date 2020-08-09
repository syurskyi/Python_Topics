class Solution:
    ___ getLeftPosition(self, nums, target
        left = 0
        right = le.(nums)-1

        w___(left <= right
            mid = left+(right-left)//2
            __(nums[mid] __ target
                __(mid-1 >= 0 and nums[mid-1] != target or mid __ 0
                    r_ mid
                right = mid-1
            ____(nums[mid] > target
                right = mid-1
            ____
                left = mid+1

        r_ -1

    ___ getRightPosition(self, nums, target
        left = 0
        right = le.(nums)-1

        w___(left <= right
            mid = left+(right-left)//2
            __(nums[mid] __ target
                __(mid+1 < le.(nums) and nums[mid+1] != target or mid __ le.(nums)-1
                    r_ mid
                left = mid+1
            ____(nums[mid] > target
                right = mid-1
            ____
                left = mid+1

        r_ -1

    ___ searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.getLeftPosition(nums, target)
        right = self.getRightPosition(nums, target)

        r_ [left, right]
