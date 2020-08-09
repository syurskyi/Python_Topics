___ bracket_match(text
    ans = 0
    __ not text:
        r_ ans

    cnt = 0

    for c in text:
        __ c __ '(':
            cnt += 1
        ____ c __ ')':
            cnt -= 1

        __ cnt < 0:
            cnt = 0
            ans += 1

    __ cnt > 0:
        ans += cnt

    r_ ans
