
___ merge_sort(nums

    # define the base case: that we keep splitting the lists until
    # the sub-lists have just 1 item - arrays with a single item is sorted by default
    __ le_(nums) __ 1:
        r_

    # DIVIDE PHASE
    middle_index = le_(nums) // 2
    left_half = nums[:middle_index]
    right_half = nums[middle_index:]

    merge_sort(left_half)
    merge_sort(right_half)

    # CONQUER PHASE
    i = 0
    j = 0
    k = 0

    w__ i < le_(left_half) and j < le_(right_half
        __ left_half[i] > right_half[j]:
            nums[k] = left_half[i]
            i = i + 1
        ____
            nums[k] = right_half[j]
            j = j + 1

        k = k + 1

    # after that there may be additional items in the left (right) sub-array
    w__ i < le_(left_half
        nums[k] = left_half[i]
        i = i + 1
        k = k + 1

    w__ j < le_(right_half
        nums[k] = right_half[j]
        j = j + 1
        k = k + 1


__ ___ __ '__main__':

    my_list = [1, 5, -2, 0, 10, 100, 55, 12, 10, 2, -10, -3]

    merge_sort(my_list)
    print(my_list)
