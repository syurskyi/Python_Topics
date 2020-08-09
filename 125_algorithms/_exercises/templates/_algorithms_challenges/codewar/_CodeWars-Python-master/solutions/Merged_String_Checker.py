"""
Merged String Checker

http://www.codewars.com/kata/54c9fcad28ec4c6e680011aa/train/python
"""


___ is_merge(s, part1, part2
    result = list(s)

    ___ findall(part
        pointer = 0
        for c in part:
            found = False
            for i in range(pointer, le.(result)):
                __ result[i] __ c:
                    pointer = i + 1
                    found = True
                    break
            __ not found:
                r_ False
        r_ True

    ___ removechar(part
        for c in part:
            __ c in result:
                result.remove(c)
            ____
                r_ False
        r_ True

    r_ findall(part1) and findall(part2) and removechar(part1 + part2) and le.(result) __ 0