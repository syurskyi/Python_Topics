from itertools ______ cycle, chain


___ fence_pattern(rails, size
    zig_zag = cycle(chain(range(rails), range(rails - 2, 0, -1)))
    r_ zip(zig_zag, range(size))


___ encode(msg, rails
    fence = fence_pattern(rails, le.(msg))
    r_ ''.join(msg[i] ___ _, i __ sorted(fence))


___ decode(msg, rails
    fence = fence_pattern(rails, le.(msg))
    fence_msg = zip(msg, sorted(fence))
    r_ ''.join(
        char ___ char, _ __ sorted(fence_msg, key=lambda item: item[1][1]))
