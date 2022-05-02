c_ Solution o..
    ___ ipToInt  ip):
        ans = 0
        ___ x __ ip.split('.'):
            ans = 256 * ans + int(x)
        r_ ans

    ___ intToIP  x):
        r_ ".".join(str((x >> i) % 256)
                        ___ i __ (24, 16, 8, 0))

    ___ ipToCIDR  ip, n):
        # Start value of IP
        start = ipToInt(ip)
        ans =    # list
        w.. n:
            # Last 1 of start or can start from 0
            mask = max(33 - (start & -start).bit_length(),
                       33 - n.bit_length())
            ans.append(intToIP(start) + '/' + str(mask))
            start += 1 << (32 - mask)
            n -= 1 << (32 - mask)
        r_ ans
