____ t___ _______ L.., T..
T T..('T', i.., f__)


___ n_digit_numbersnumbers L.. T n i.. __ L.. i..
    # Checks
    __ n < 1:
        r.. V...

    __ numbers __ []:
        r.. []

    n_multiply_lookup {1: 1, 2: 10, 3: 100, 4: 1000}

    ___ i __ r..(l..(numbers:
        numbers[i] r..(numbers[i] * n_multiply_lookup[n])
        __ l..(s..(numbers[i] > n:
            __ numbers[i] > 0:
                numbers[i] i..(s..(numbers[i]) :?)
            ____
                numbers[i] i..(s..(numbers[i]) |? +1])

    r.. numbers

#if __name__ == "__main__":
    #print(n_digit_numbers([], 2))
    #print(n_digit_numbers([1, 2, 3], 1))
    #print(n_digit_numbers([1, 2, 3], 2))
    #print(n_digit_numbers([0, 1, 2, 3], 2))
    #print(n_digit_numbers([8, 9, 10], 2))
    #print(n_digit_numbers([5.2, 1600, 520, 3600, 13, 55, 4000], 2))
    #print(n_digit_numbers([-1.1, 2.22, -3.333], 3))
    #print(n_digit_numbers([-1.1, 2.22, -3.333, 4444, 55555], 4))