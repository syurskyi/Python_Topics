class Solution:
    """
    @param array: an integer array
    @return: the length of the minimum cycle section
    """
    ___ minimumCycleSection(self, array
        __ not array:
            r_ 0

        n = le.(array)

        for size in range(1, n + 1
            gotcha = True

            for i in range(size
                __ any(array[i] != array[j] for j in range(i + size, n, size)):
                    gotcha = False

            __ gotcha:
                r_ size

        r_ n
