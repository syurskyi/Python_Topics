"""
Merged String Checker

http://www.codewars.com/kata/54c9fcad28ec4c6e680011aa/train/python
"""


___ is_merge(s, part1, part2):
    result = l..(s)

    ___ findall(part):
        pointer = 0
        ___ c __ part:
            found = False
            ___ i __ r..(pointer, l..(result)):
                __ result[i] __ c:
                    pointer = i + 1
                    found = True
                    break
            __ n.. found:
                r.. False
        r.. True

    ___ removechar(part):
        ___ c __ part:
            __ c __ result:
                result.remove(c)
            ____:
                r.. False
        r.. True

    r.. findall(part1) a.. findall(part2) a.. removechar(part1 + part2) a.. l..(result) __ 0