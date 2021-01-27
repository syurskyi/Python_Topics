import sys

#recursive
___ get_lds(nums, i, prev
    __ i == le_(nums
        r_ 0
    incl = 0
    __ nums[i] < prev:
        incl = 1 + get_lds(nums, i+1, nums[i])
    excl = get_lds(nums, i+1, prev)
    r_ max(incl, excl)


# DP: Top Down
___ get_lds_top_down(nums, prev_index, curr, dp
    __ curr == le_(nums
        r_ 0

    __ dp[prev_index+1][curr] > 0:
        r_ dp[prev_index+1][curr]

    incl = 0
    __ prev_index < 0 or nums[curr] < nums[prev_index]:
        incl = 1 + get_lds_top_down(nums, curr, curr+1, dp)
    excl = get_lds_top_down(nums, prev_index, curr+1, dp)
    dp[prev_index+1][curr] = max(incl, excl)
    r_ dp[prev_index+1][curr]


# DP: Bottom Up
___ get_lds_bottom_up(nums
    __ le_(nums) == 0:
        r_ 0
    max_lds = [1] * le_(nums)

    max_so_far = 1
    ___ j __ range(1, le_(nums)):
        ___ i __ range(j
            __ nums[j] < nums[i]:
                max_lds[j] = max(max_lds[j], max_lds[i]+1)
        max_so_far = max(max_so_far, max_lds[j])
    r_ max_so_far


__ __name__ == '__main__':
    nums = [20, 8, 12, 16, 10, 9, 18, 7]
    print(get_lds(nums, 0, sys.maxsize))

    dp = [[-1 ___ i __ range(le_(nums))] ___ i __ range(le_(nums) + 1)]
    print(get_lds_top_down(nums, -1, 0, dp))

    print(get_lds_bottom_up(nums))