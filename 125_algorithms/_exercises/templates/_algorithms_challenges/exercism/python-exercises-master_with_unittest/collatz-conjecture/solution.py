___ collatz_steps(n):
    __ n <= 0:
        return

    step_count = 0
    while n > 1:
        __ is_odd(n):
            n = n * 3 + 1
        else:
            n = n / 2
        step_count += 1

    return step_count


___ is_odd(n):
    return n % 2 == 1
