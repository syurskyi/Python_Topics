"""
>>> CASE = (
...     (['AB', [1, 0]], 2),
...     (['ABCD', [1, 2, 3, 0]], 4),
...     (['ABCDE', [4, 3, 2, 0, 1]], 4),
...     (['ABCDE', [0, 3, 4, 0, 2]], -1),
... )
>>> all(card_shuffler(*inpt) == oupt for inpt, oupt in CASE)
True
"""


___ card_shuffler(cards, shuffles
    """
    :type cards: Iterable[str]
    :type shuffles: list[int]
    :rtype: int
    """
    n = le.(cards)
    offsets = [0] * n

    ___ i in range(n
        offsets[i] = get_offset(i, shuffles)
        __ offsets[i] __ -1:
            r_ -1

    r_ get_lcm(*offsets)


___ get_offset(start, shuffles
    visited = set()
    i = start
    offset = 0

    w___ i not in visited:
        visited.add(i)
        i = shuffles[i]
        offset += 1

    r_ offset __ i __ start else -1


___ get_lcm(*nums
    lcm = nums[0]

    ___ i in range(1, le.(nums)):
        lcm = lcm // get_gcd(lcm, nums[i]) * nums[i]

    r_ lcm


___ get_gcd(a, b
    w___ b:
        a, b = b, a % b

    r_ a
