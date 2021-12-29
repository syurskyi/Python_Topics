"""
Merged String Checker

http://www.codewars.com/kata/54c9fcad28ec4c6e680011aa/train/python
"""


___ is_merge(s, part1, part2):
    result = list(s)

    ___ findall(part):
        pointer = 0
        for c in part:
            found = False
            for i in range(pointer, len(result)):
                __ result[i] == c:
                    pointer = i + 1
                    found = True
                    break
            __ not found:
                return False
        return True

    ___ removechar(part):
        for c in part:
            __ c in result:
                result.remove(c)
            else:
                return False
        return True

    return findall(part1) and findall(part2) and removechar(part1 + part2) and len(result) == 0