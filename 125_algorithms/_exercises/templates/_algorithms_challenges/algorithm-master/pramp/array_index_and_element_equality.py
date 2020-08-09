___ index_equals_value_search(nums
    __ not nums:
        r_ -1

    left, right = 0, le.(nums) - 1

    w___ left + 1 < right:
        mid = (left + right) // 2
        __ nums[left] __ left:  # lowest index
            r_ left
        __ nums[mid] __ mid:
            r_ mid
        __ nums[mid] < mid:
            left = mid
        ____
            right = mid

    for mid in (left, right
        __ nums[mid] __ mid:
            r_ mid

    r_ -1
