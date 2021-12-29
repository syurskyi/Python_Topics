"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.
"""
__author__ = 'Danyang'
class Solution:
    ___ longestConsecutive_TLE(self, num):
        """
        O(n) within in one scan
        algorithm: array, inverted index
        O(kn), k is the length of consecutive sequence

        TLE due to excessive lookup

        :param num: a list of integer
        :return: an integer
        """
        length = l..(num)
        inverted_table = d..(z..(num, r..(length)))

        max_length = -1<<31
        ___ ind, val __ e..(num):
            current_length = 1
            # check val--
            sequence_val_expected = val-1
            w.... sequence_val_expected __ inverted_table:
                sequence_val_expected -= 1
                current_length += 1

            # check val++
            sequence_val_expected = val+1
            w.... sequence_val_expected __ inverted_table:
                sequence_val_expected += 1
                current_length += 1

            max_length = max(max_length, current_length)

        r.. max_length

    ___ longestConsecutive(self, num):
        """
        Algorithm: pivot scanning
        array, inverted index (visited)
        O(n) within in one scan
        O(kn), k is the length of consecutive sequence

        visited map

        :param num: a list of integer
        :return: an integer
        """
        visited = {item: False ___ item __ num}

        max_length = -1<<31
        ___ ind, val __ e..(num):
            __ visited[val]: continue

            current_length = 1

            # check val--
            sequence_val_expected = val-1
            w.... sequence_val_expected __ visited:
                visited[sequence_val_expected] = True
                sequence_val_expected -= 1
                current_length += 1

            # check val++
            sequence_val_expected = val+1
            w.... sequence_val_expected __ visited:
                visited[sequence_val_expected] = True
                sequence_val_expected += 1
                current_length += 1

            max_length = max(max_length, current_length)

        r.. max_length

