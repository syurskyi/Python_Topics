c_ Solution:
    # @param an integer
    # @return a list of string
    ___ generateParenthesis  n
        cand    # list
        res    # list
        generate_paren_aux(n, n, cand, res)
        r.. res

    ___ generate_paren_aux  left, right, cand, res
        __ left __ 0 a.. right __ 0:
            res.a..(''.j..(cand
        ____
            __ left <_ right a.. left > 0
                cand.a..('(')
                generate_paren_aux(left - 1, right, cand, res)
                cand.p.. )
            __ left < right a.. right > 0
                cand.a..(')')
                generate_paren_aux(left, right - 1, cand, res)
                cand.p.. )
