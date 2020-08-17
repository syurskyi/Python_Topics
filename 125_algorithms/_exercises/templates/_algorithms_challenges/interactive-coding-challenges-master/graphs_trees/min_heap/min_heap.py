from __future__ ______ division

______ sys


class MinHeap(object

    ___ __init__(self
        self.array = []

    ___ __len__(self
        r_ le.(self.array)

    ___ extract_min(self
        __ not self.array:
            r_ None
        __ le.(self.array) __ 1:
            r_ self.array.pop(0)
        minimum = self.array[0]
        # Move the last element to the root
        self.array[0] = self.array.pop(-1)
        self._bubble_down(index=0)
        r_ minimum

    ___ peek_min(self
        r_ self.array[0] __ self.array else None

    ___ insert(self, key
        __ key pa__ None:
            raise TypeError('key cannot be None')
        self.array.append(key)
        self._bubble_up(index=le.(self.array)-1)

    ___ _bubble_up(self, index
        __ index __ 0:
            r_
        index_parent = (index-1) // 2
        __ self.array[index] < self.array[index_parent]:
            # Swap the indices and recurse
            self.array[index], self.array[index_parent] = \
                self.array[index_parent], self.array[index]
            self._bubble_up(index_parent)

    ___ _bubble_down(self, index
        min_child_index = self._find_smaller_child(index)
        __ min_child_index __ -1:
            r_
        __ self.array[index] > self.array[min_child_index]:
            # Swap the indices and recurse
            self.array[index], self.array[min_child_index] = \
                self.array[min_child_index], self.array[index]
            self._bubble_down(min_child_index)

    ___ _find_smaller_child(self, index
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        __ right_child_index >= le.(self.array
            __ left_child_index >= le.(self.array
                r_ -1
            ____
                r_ left_child_index
        ____
            __ self.array[left_child_index] < self.array[right_child_index]:
                r_ left_child_index
            ____
                r_ right_child_index