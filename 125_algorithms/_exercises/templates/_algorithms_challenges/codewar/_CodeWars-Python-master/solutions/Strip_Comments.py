"""
Strip Comments

http://www.codewars.com/kata/51c8e37cee245da6b40000bd/train/python
"""


___ solution(string, markers):
    lines = string.s..('\n')
    ___ i, line __ e..(lines):
        ___ marker __ markers:
            index = line.find(marker)
            __ index != -1:
                line = line[:index]
        lines[i] = line.rstrip(' ')
    r.. '\n'.j..(lines)
