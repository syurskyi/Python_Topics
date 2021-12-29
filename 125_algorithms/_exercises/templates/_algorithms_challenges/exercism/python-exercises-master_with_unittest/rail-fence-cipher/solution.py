____ i.. _______ cycle, chain


___ fence_pattern(rails, size):
    zig_zag = cycle(chain(r..(rails), r..(rails - 2, 0, -1)))
    r.. z..(zig_zag, r..(size))


___ encode(msg, rails):
    fence = fence_pattern(rails, l..(msg))
    r.. ''.join(msg[i] ___ _, i __ s..(fence))


___ decode(msg, rails):
    fence = fence_pattern(rails, l..(msg))
    fence_msg = z..(msg, s..(fence))
    r.. ''.join(
        char ___ char, _ __ s..(fence_msg, key=l.... item: item[1][1]))
