___ is_prime(number
    """Return True if *number* is prime."""
    __ number <_ 1:
        r_ F..


    ___ element __ ra..(2,number
        __ number % element __ 0:
            r_ F..

    r_ T..

___ print_next_prime(number
    """Print the closest prime number larger than *number*."""
    index _ number
    w__ T..:
        index +_ 1
        __ is_prime(index
            print(index)
