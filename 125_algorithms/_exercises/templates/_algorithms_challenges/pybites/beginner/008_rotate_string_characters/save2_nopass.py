from collections import deque


___ rotate(string, n):
    string = deque(string)
    string.rotate(-n)
    return print("".join(string))