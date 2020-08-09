class Solution:
    ___ isPalin(self, seg
        i = 0
        j = le.(seg)-1
        w___(i < j
            __(seg[i] != seg[j]
                r_ False
            i += 1
            j -= 1
        r_ True

    ___ dfs(self, s: str
        __(le.(s) __ 0 and le.(self.temp) > 0
            self.res.append(self.temp[:])
            r_
        n = le.(s)+1
        for i in range(1, n
            seg = s[0:i]
            __(self.isPalin(seg)):
                self.temp.append(seg)
                self.dfs(s[i:])
                self.temp.pop()

    ___ partition(self, s: str) -> List[List[str]]:
        self.res = []
        self.temp = []
        self.dfs(s)
        r_ self.res
