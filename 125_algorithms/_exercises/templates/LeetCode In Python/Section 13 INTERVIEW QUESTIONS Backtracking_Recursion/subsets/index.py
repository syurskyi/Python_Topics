c_ Solution:
    ___ solution(,nums,ans,cur,index
        __(index>le.(nums)):
            r_
        ans.ap..(cur[:])
        ___ i __ ra..(index,le.(nums)):
            __(nums[i] no. __ cur
                cur.ap..(nums[i])
                .solution(nums,ans,cur,i)
                cur.pop()
        r_
    ___ subsets(, nums: L.. in.) -> L..[L..[in.]]:
        ans _ []
        cur _ []
        .solution(nums,ans,cur,0)
        r_ ans