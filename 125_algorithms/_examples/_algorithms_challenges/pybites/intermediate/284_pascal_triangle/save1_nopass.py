from typing import List

def pascal(N: int) -> List[int]:
    """
    Return the Nth row of Pascal triangle
    """
    if N == 1:
        return [1]
    else:
        line = [1]
        previous_line = pascal(N - 1)
        for i in range(len(previous_line) - 1):
            line.append(previous_line[i] + previous_line[i + 1])
        line += [1]
    return line