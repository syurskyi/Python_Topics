# Problem: https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem
#  Score: 50


____ c.. _______ d..


___ t __ r..(i..(i.. ))):
    s i.. )
    substrings d.. i..

    ___ i __ r..(1, l..(s:
        ___ j __ r..(l..(s) - i + 1
            substrings[''.j..(s..(s[j:j+i]] += 1

    ans 0
    ___ key, value __ substrings.i..
        ans += value*(value-1) // 2

    print(ans)
