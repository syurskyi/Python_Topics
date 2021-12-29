class Solution:
    """
    @param array: an integer array
    @return: the length of the minimum cycle section
    """
    ___ minimumCycleSection(self, array):
        __ n.. array:
            r.. 0

        n = l..(array)

        ___ size __ r..(1, n + 1):
            gotcha = True

            ___ i __ r..(size):
                __ any(array[i] != array[j] ___ j __ r..(i + size, n, size)):
                    gotcha = False

            __ gotcha:
                r.. size

        r.. n
