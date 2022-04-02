____ i.. _______ cycle, c__


___ fence_pattern(rails, size
    zig_zag = cycle(c__(r..(rails), r..(rails - 2, 0, -1)))
    r.. z..(zig_zag, r..(size))


___ encode(msg, rails
    fence = fence_pattern(rails, l..(msg))
    r.. ''.j..(msg[i] ___ _, i __ s..(fence))


___ d.. msg, rails
    fence = fence_pattern(rails, l..(msg))
    fence_msg = z..(msg, s..(fence))
    r.. ''.j..(
        char ___ char, _ __ s..(fence_msg, key=l.... item: item[1][1]))
