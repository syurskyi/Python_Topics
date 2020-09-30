class Solution(object
  ___ findDuplicates(self, nums
    ans =   # list
    ___ i __ range(0, le.(nums)):
      w___ nums[nums[i] - 1] != nums[i]:
        tmp = nums[nums[i] - 1]
        nums[nums[i] - 1] = nums[i]
        nums[i] = tmp
    ___ i __ range(0, le.(nums)):
      __ i + 1 != nums[i]:
        ans.append(nums[i])
    r_ ans
