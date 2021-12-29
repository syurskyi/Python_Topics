from itertools import cycle, chain


___ fence_pattern(rails, size):
    zig_zag = cycle(chain(range(rails), range(rails - 2, 0, -1)))
    return zip(zig_zag, range(size))


___ encode(msg, rails):
    fence = fence_pattern(rails, len(msg))
    return ''.join(msg[i] for _, i in sorted(fence))


___ decode(msg, rails):
    fence = fence_pattern(rails, len(msg))
    fence_msg = zip(msg, sorted(fence))
    return ''.join(
        char for char, _ in sorted(fence_msg, key=lambda item: item[1][1]))
