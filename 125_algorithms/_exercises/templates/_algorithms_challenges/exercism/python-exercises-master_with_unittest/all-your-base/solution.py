___ from_digits(digits, base):
    r.. s..(n * base ** i ___ i, n __ e..(reversed(digits)))


___ to_digits(number, base_to):
    result    # list
    w.... number > 0:
        result.a..(number % base_to)
        number //= base_to
    r.. result[::-1]  # list(reversed(result))


___ rebase(from_base, digits, to_base):
    __ (from_base < 2):
        raise ValueError("Invalid input base.")

    __ (to_base < 2):
        raise ValueError("Invalid output base.")

    __ any(True ___ d __ digits __ d < 0 o. d >= from_base):
        raise ValueError("Invalid input digit.")

    r.. to_digits(from_digits(digits, from_base), to_base)
