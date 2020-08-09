class Solution:
    ___ solution(self, candidates,ans,cur,target,index,sum
        __(sum__target
            ans.append(cur[:])
        ____(sum<target
            n = le.(candidates)
            for i in range(index,n
                cur.append(candidates[i])
                self.solution(candidates,ans,cur,target,i,sum+candidates[i])
                cur.pop()
        r_
    ___ combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        cur = []
        self.solution(candidates,ans,cur,target,0,0)
        r_ ans