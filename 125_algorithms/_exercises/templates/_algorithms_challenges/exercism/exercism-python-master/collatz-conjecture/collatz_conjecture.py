from itertools ______ count

___ collatz_steps(number
    __ number <= 0:
        raise ValueError(
                "Number must be greater then 0: collatz_steps({})".format(number))
    ___ step in count(0
        __ number __ 1:
            r_ step
        number = number / 2 __ number % 2 __ 0 else 3 * number + 1
