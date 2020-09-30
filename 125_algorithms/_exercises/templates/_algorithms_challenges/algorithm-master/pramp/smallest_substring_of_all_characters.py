___ get_shortest_unique_substring(strs, s
    __ not strs or not s:
        r_ ''

    freq = dict.fromkeys(strs, 0)
    left = cnt = 0
    start = 0
    size = INF = float('inf')

    ___ right __ range(le.(s)):
        __ s[right] __ freq:
            __ freq[s[right]] __ 0:
                cnt += 1
            freq[s[right]] += 1

        w___ cnt __ le.(freq
            __ right - left + 1 < size:
                start = left
                size = right - left + 1

            __ s[left] __ freq:
                freq[s[left]] -= 1
                __ freq[s[left]] __ 0:
                    cnt -= 1

            left += 1

    r_ s[start:start + size] __ size < INF else ''
