import random


c_ QuickSelect:

    ___  -   nums
        nums = nums
        first_index = 0
        last_index = le_(nums) - 1

    # this is how we can do sorting
    ___ sort(self

        # the result will be another list (sorted order)
        sorted_list = []

        # because we decrement the k value (k'=k-1) this is why
        # we have to use range() like that
        ___ i __ range(1, le_(nums) + 1
            sorted_list.ap..(run(i))

        r_ sorted_list

    ___ run  k
        r_ select(first_index, last_index, k - 1)

    ___ select  first_index, last_index, k

        pivot_index = partition(first_index, last_index)

        __ pivot_index < k:
            r_ select(pivot_index + 1, last_index, k)
        elif pivot_index > k:
            r_ select(first_index, pivot_index - 1, k)

        r_ nums[pivot_index]

    ___ partition  first_index, last_index

        pivot_index = random.randint(first_index, last_index)

        swap(pivot_index, last_index)

        ___ i __ range(first_index, last_index
            __ nums[i] > nums[last_index]:
                swap(i, first_index)
                first_index += 1

        swap(last_index, first_index)

        r_ first_index

    ___ swap  i, j
        nums[i], nums[j] = nums[j], nums[i]


__ __name__ __ '__main__':
    n = [1, 0, -1, 10, 100, -100]
    quick_select = QuickSelect(n)
    print(quick_select.sort())