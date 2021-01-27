import random


c_ QuickSelect:

    ___  -   nums
        nums = nums
        first_index = 0
        last_index = le_(nums) - 1

    ___ run  k
        r_ select(first_index, last_index, k-1)

    # PARTITION PHASE
    ___ partition  first_index, last_index

        # generate a random value within the range [first, last]
        pivot_index = random.randint(first_index, last_index)

        swap(pivot_index, last_index)

        ___ i __ range(first_index, last_index
            __ nums[i] > nums[last_index]:
                swap(i, first_index)
                first_index += 1

        swap(first_index, last_index)

        # it is the index of the pivot
        r_ first_index

    ___ swap  i, j
        nums[i], nums[j] = nums[j], nums[i]

    # THIS IS THE SELECTION PHASE
    ___ select  first_index, last_index, k

        pivot_index = partition(first_index, last_index)

        # selection phase when we compare the pivot_index with k
        __ pivot_index < k:
            # we have to discard the left sub-array and keep
            # considering the items on the right
            r_ select(pivot_index + 1, last_index, k)
        elif pivot_index > k:
            # we have to discard the right sub-array
            r_ select(first_index, pivot_index - 1, k)

        # we have found the item we are looking for
        r_ nums[pivot_index]


x = [1, 2, -5, 10, 100, -7, 3, 4]
select = QuickSelect(x)
print(select.run(2))

