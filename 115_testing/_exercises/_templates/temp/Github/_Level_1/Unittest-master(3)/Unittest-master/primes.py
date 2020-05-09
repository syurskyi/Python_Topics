___ is_prime(number
    """Return True if *number* is prime."""
    __ number <_ 1:
        r_ False


    for element in range(2,number
        __ number % element __ 0:
            r_ False

    r_ True

___ print_next_prime(number
    """Print the closest prime number larger than *number*."""
    index _ number
    while True:
        index +_ 1
        __ is_prime(index
            print(index)
