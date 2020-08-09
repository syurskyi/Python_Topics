class Solution:
    ___ solution(self, candidates,ans,cur,target,index,su.
        __(sum__target
            ans.append(cur[:])
        ____(su.<target
            n = le.(candidates)
            ___ i __ ra..(index,n
                cur.append(candidates[i])
                self.solution(candidates,ans,cur,target,i,su.+candidates[i])
                cur.pop()
        r_
    ___ combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        cur = []
        self.solution(candidates,ans,cur,target,0,0)
        r_ ans