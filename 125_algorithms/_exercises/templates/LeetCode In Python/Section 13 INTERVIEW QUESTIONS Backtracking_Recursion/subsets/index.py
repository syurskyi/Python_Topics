class Solution:
    ___ solution(self,nums,ans,cur,index
        __(index>le.(nums)):
            r_
        ans.append(cur[:])
        ___ i __ ra..(index,le.(nums)):
            __(nums[i] not __ cur
                cur.append(nums[i])
                self.solution(nums,ans,cur,i)
                cur.pop()
        r_
    ___ subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        cur = []
        self.solution(nums,ans,cur,0)
        r_ ans