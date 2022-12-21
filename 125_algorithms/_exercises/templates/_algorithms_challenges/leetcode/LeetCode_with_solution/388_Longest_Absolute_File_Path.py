c_ Solution o..
    ___ lengthLongestPath  input
        """
        :type input: str
        :rtype: int
        """
        __ input is N.. or l.. input) __ 0:
            r_ 0
        lines = input.split('\n')
        last_level_len = [0] * (l.. lines) + 1); max_len = 0
        ___ line __ lines:
            try:
                level = line.rindex('\t') + 1
            except:
                level = 0
            cur_len = last_level_len[level + 1] = last_level_len[level] + l.. line) - level + 1
            __ '.' __ line:
                max_len = m..(max_len, cur_len - 1)
        r_ max_len

__ ____ __ ____
    s  ?
    print s.lengthLongestPath("dir\n    file.txt")
