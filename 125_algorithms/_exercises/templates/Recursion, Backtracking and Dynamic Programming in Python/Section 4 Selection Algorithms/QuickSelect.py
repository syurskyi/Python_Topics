import random


class QuickSelect:

    ___ __init__(self, nums
        self.nums = nums
        self.first_index = 0
        self.last_index = le_(nums) - 1

    ___ run(self, k
        r_ self.select(self.first_index, self.last_index, k-1)

    # PARTITION PHASE
    ___ partition(self, first_index, last_index

        # generate a random value within the range [first, last]
        pivot_index = random.randint(first_index, last_index)

        self.swap(pivot_index, last_index)

        ___ i __ range(first_index, last_index
            __ self.nums[i] > self.nums[last_index]:
                self.swap(i, first_index)
                first_index += 1

        self.swap(first_index, last_index)

        # it is the index of the pivot
        r_ first_index

    ___ swap(self, i, j
        self.nums[i], self.nums[j] = self.nums[j], self.nums[i]

    # THIS IS THE SELECTION PHASE
    ___ select(self, first_index, last_index, k

        pivot_index = self.partition(first_index, last_index)

        # selection phase when we compare the pivot_index with k
        __ pivot_index < k:
            # we have to discard the left sub-array and keep
            # considering the items on the right
            r_ self.select(pivot_index + 1, last_index, k)
        elif pivot_index > k:
            # we have to discard the right sub-array
            r_ self.select(first_index, pivot_index - 1, k)

        # we have found the item we are looking for
        r_ self.nums[pivot_index]


x = [1, 2, -5, 10, 100, -7, 3, 4]
select = QuickSelect(x)
print(select.run(2))

