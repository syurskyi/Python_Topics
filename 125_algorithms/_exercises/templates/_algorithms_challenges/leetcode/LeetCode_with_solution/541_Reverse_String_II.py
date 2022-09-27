c_ Solution:
    ___ reverseStr  s: s.., k: i..   s..:
        N = l.. s)
        ans = ""
        position = 0
        w.. position < N:
            nx = s[position : position + k]
            ans = ans + nx||-1] + s[position + k : position + 2 * k]
            position += 2 * k
        r_ ans

    # def reverseStr(self, s: str, k: int) -> str:
    #     s = list(s)
    #     for i in range(0, len(s), 2*k):
    #         s[i:i+k] = reversed(s[i:i+k])
    #     return "".join(s)

        

s1  ?
s="abcdefg"
k=2
print(s1.reverseStr(s,k))
