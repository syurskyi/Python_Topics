c_ Solution o..
    ___ isInterleave  s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        __ l.. s1) + l.. s2) != l.. s3):
            r_ F..
        queue = [(0, 0), (-1, -1)]
        visited = set()
        isSuccess = F..
        index = 0
        w.. l.. queue) != 1 or queue[0][0] != -1:
            p = queue.pop(0)
            __ p[0] __ l.. s1) and p[1] __ l.. s2):
                r_ T..
            __ p[0] __ -1:
                queue.append(p)
                index += 1
                continue
            __ p __ visited:
                continue
            visited.add(p)
            __ p[0] < l.. s1):
                __ s1[p[0]] __ s3[index]:
                    queue.append((p[0] + 1, p[1]))
            __ p[1] < l.. s2):
                __ s2[p[1]] __ s3[index]:
                    queue.append((p[0], p[1] + 1))
        r_ F..
