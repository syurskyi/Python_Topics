___ from_digits(digits, base
    r_ su.(n * base ** i ___ i, n in enumerate(reversed(digits)))


___ to_digits(number, base_to
    result = []
    w___ number > 0:
        result.append(number % base_to)
        number //= base_to
    r_ result[::-1]  # list(reversed(result))


___ rebase(from_base, digits, to_base
    __ (from_base < 2
        raise ValueError("Invalid input base.")

    __ (to_base < 2
        raise ValueError("Invalid output base.")

    __ any(True ___ d in digits __ d < 0 or d >= from_base
        raise ValueError("Invalid input digit.")

    r_ to_digits(from_digits(digits, from_base), to_base)
