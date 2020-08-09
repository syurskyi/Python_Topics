class Solution:

    ___ backtracking(self, ans, m, digits, combination, index
        __(index > le.(digits)):
            r_
        __(le.(combination) __ le.(digits)):
            ans.append(combination[:])
            r_

        currentDigit = digits[index]
        curString = m[currentDigit]

        ___ i __ ra..(le.(curString)):
            self.backtracking(ans, m, digits, combination +
                              curString[i], index+1)

    ___ letterCombinations(self, digits: str) -> List[str]:
        ans = []
        __(le.(digits) __ 0
            r_ ans

        m = {}

        m['2'] = "abc"
        m['3'] = "___"
        m['4'] = "ghi"
        m['5'] = "jkl"
        m['6'] = "mno"
        m['7'] = "pqrs"
        m['8'] = "tuv"
        m['9'] = "wxyz"

        self.backtracking(ans, m, digits, "", 0)

        r_ ans
