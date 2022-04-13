___ from_digits(d.., base
    r.. s..(n * base ** i ___ i, n __ e..(r..(d..)))


___ to_digits(number, base_to
    result    # list
    w.... number > 0
        result.a..(number % base_to)
        number //= base_to
    r.. result[::-1]  # list(reversed(result))


___ rebase(from_base, d.., to_base
    __ (from_base < 2
        r.. V...("Invalid input base.")

    __ (to_base < 2
        r.. V...("Invalid output base.")

    __ a__(T.. ___ d __ d.. __ d < 0 o. d >_ from_base
        r.. V...("Invalid input digit.")

    r.. to_digits(from_digits(d.., from_base), to_base)
