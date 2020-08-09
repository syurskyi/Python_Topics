c_ Solution:
    ___ solution(, candidates,ans,cur,target,index,su.
        __(sum__target
            ans.ap..(cur[:])
        ____(su.<target
            n _ le.(candidates)
            ___ i __ ra..(index,n
                cur.ap..(candidates[i])
                .solution(candidates,ans,cur,target,i,su.+candidates[i])
                cur.pop()
        r_
    ___ combinationSum(, candidates: L.. in., target: in.)  L..[L..[in.]]:
        ans _   # list
        cur _   # list
        .solution(candidates,ans,cur,target,0,0)
        r_ ans