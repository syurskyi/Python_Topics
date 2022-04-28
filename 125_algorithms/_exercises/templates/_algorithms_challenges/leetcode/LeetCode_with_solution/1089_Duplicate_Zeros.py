c_ Solution:
    ___ duplicateZeros  arr: List[int]) -> N..:
        """
        Do not return anything, modify arr in-place instead.
        """
        move_pos = 0
        last_pos = l.. arr) - 1
        ___ i __ r.. last_pos + 1):
            # Only check [0, lastPos - movePos]
            __ i > last_pos - move_pos:
                break
            __ arr[i] __ 0:
                # Special case
                __ i __ last_pos - move_pos:
                    arr[last_pos] = 0
                    last_pos -= 1
                    break
                move_pos += 1
        last_pos -= move_pos
        ___ i __ r.. last, -1, -1):
            __ arr[i] __ 0:
                arr[i + move_pos] = 0
                move_pos -= 1
                arr[i + move_pos] = 0
            ____
                arr[i + move_pos] = arr[i]
