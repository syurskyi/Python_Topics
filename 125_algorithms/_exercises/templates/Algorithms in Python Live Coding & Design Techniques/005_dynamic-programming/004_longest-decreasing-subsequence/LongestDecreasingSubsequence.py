_____ sys

#recursive
___ get_lds(nums, i, prev
    __ i __ le_(nums
        r_ 0
    incl  0
    __ nums[i] < prev:
        incl  1 + get_lds(nums, i+1, nums[i])
    excl  get_lds(nums, i+1, prev)
    r_ ma_(incl, excl)


# DP: Top Down
___ get_lds_top_down(nums, prev_index, curr, dp
    __ curr __ le_(nums
        r_ 0

    __ dp[prev_index+1][curr] > 0:
        r_ dp[prev_index+1][curr]

    incl  0
    __ prev_index < 0 o. nums[curr] < nums[prev_index]:
        incl  1 + get_lds_top_down(nums, curr, curr+1, dp)
    excl  get_lds_top_down(nums, prev_index, curr+1, dp)
    dp[prev_index+1][curr]  ma_(incl, excl)
    r_ dp[prev_index+1][curr]


# DP: Bottom Up
___ get_lds_bottom_up(nums
    __ le_(nums) __ 0:
        r_ 0
    max_lds  [1] * le_(nums)

    max_so_far  1
    ___ j __ ra__(1, le_(nums)):
        ___ i __ ra__(j
            __ nums[j] < nums[i]:
                max_lds[j]  ma_(max_lds[j], max_lds[i]+1)
        max_so_far  ma_(max_so_far, max_lds[j])
    r_ max_so_far


__ ___ __ '__main__':
    nums  [20, 8, 12, 16, 10, 9, 18, 7]
    print(get_lds(nums, 0, sys.maxsize))

    dp  [[-1 ___ i __ ra__(le_(nums))] ___ i __ ra__(le_(nums) + 1)]
    print(get_lds_top_down(nums, -1, 0, dp))

    print(get_lds_bottom_up(nums))