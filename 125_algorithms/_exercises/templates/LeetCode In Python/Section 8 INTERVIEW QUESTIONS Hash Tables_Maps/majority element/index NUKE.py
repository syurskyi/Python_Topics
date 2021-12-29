class Solution:
    def majorityElement(self, nums: List[i..]) -> i..:
        m  {}
        for num in nums:
            m[num]  m.get(num,0)+1
        for num in nums:
            __(m[num]>len(nums)//2):
                return num
        
                