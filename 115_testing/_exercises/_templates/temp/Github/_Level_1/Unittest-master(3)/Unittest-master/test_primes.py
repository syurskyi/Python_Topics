______ u__
____ primes ______ is_prime

c_ PrimesTestCase?.?
    """Tests for `primes.py`."""

    ___ test_is_five_prime
        """Is five successfully determined to be prime?"""
        aT..(is_prime(5))

    ___ test_is_four_non_prime
        """Is four correctly determined not to be prime?"""
        aF..(is_prime(4), msg_'Four is not prime!')

    ___ test_is_zero_not_prime
        """Is zero correctly determined not to be prime?"""
        aF..(is_prime(0))

    ___ test_negative_number
        """Is a negative number correctly determined not to be prime?"""
        ___ index __ ra..(-1, -10, -1
            aF..(is_prime(index), msg_'{} should not be determined to be prime'.f..(index))

__ _____ __ _____
    ?.?
