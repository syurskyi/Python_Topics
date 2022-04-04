___ collatz_steps(n
    __ n <= 0:
        r..

    step_count = 0
    w.... n > 1:
        __ is_odd(n
            n = n * 3 + 1
        ____
            n = n / 2
        step_count += 1

    r.. step_count


___ is_odd(n
    r.. n % 2 __ 1
