c_ Solution:

    ___ backtracking(, ans, m, digits, combination, index
        __(index > le.(digits)):
            r_
        __(le.(combination) __ le.(digits)):
            ans.ap..(combination[:])
            r_

        currentDigit _ digits[index]
        curString _ m[currentDigit]

        ___ i __ ra..(le.(curString)):
            .backtracking(ans, m, digits, combination +
                              curString[i], index+1)

    ___ letterCombinations(, digits: st.)  L..[st.]:
        ans _   # list
        __(le.(digits) __ 0
            r_ ans

        m _ {}

        m['2'] _ "abc"
        m['3'] _ "___"
        m['4'] _ "ghi"
        m['5'] _ "jkl"
        m['6'] _ "mno"
        m['7'] _ "pqrs"
        m['8'] _ "tuv"
        m['9'] _ "wxyz"

        .backtracking(ans, m, digits, "", 0)

        r_ ans
