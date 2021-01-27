import random


class QuickSelect:

    ___ __init__(self, nums
        self.nums = nums
        self.first_index = 0
        self.last_index = le_(nums) - 1

    # this is how we can do sorting
    ___ sort(self

        # the result will be another list (sorted order)
        sorted_list = []

        # because we decrement the k value (k'=k-1) this is why
        # we have to use range() like that
        ___ i __ range(1, le_(self.nums) + 1
            sorted_list.append(self.run(i))

        r_ sorted_list

    ___ run(self, k
        r_ self.select(self.first_index, self.last_index, k - 1)

    ___ select(self, first_index, last_index, k

        pivot_index = self.partition(first_index, last_index)

        __ pivot_index < k:
            r_ self.select(pivot_index + 1, last_index, k)
        elif pivot_index > k:
            r_ self.select(first_index, pivot_index - 1, k)

        r_ self.nums[pivot_index]

    ___ partition(self, first_index, last_index

        pivot_index = random.randint(first_index, last_index)

        self.swap(pivot_index, last_index)

        ___ i __ range(first_index, last_index
            __ self.nums[i] > self.nums[last_index]:
                self.swap(i, first_index)
                first_index += 1

        self.swap(last_index, first_index)

        r_ first_index

    ___ swap(self, i, j
        self.nums[i], self.nums[j] = self.nums[j], self.nums[i]


__ __name__ == '__main__':
    n = [1, 0, -1, 10, 100, -100]
    quick_select = QuickSelect(n)
    print(quick_select.sort())