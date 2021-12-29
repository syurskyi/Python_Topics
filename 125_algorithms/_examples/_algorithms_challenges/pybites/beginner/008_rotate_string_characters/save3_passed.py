from collections import deque


def rotate(string, n):
    string = deque(string)
    string.rotate(-n)
    return "".join(string)