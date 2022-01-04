____ typing _______ List, TypeVar
T = TypeVar('T', i.., float)


___ n_digit_numbers(numbers: List[T], n: i..) __ List[i..]:
    # Checks
    __ n < 1:
        r.. ValueError

    __ numbers __ []:
        r.. []

    n_multiply_lookup = {1: 1, 2: 10, 3: 100, 4: 1000}

    ___ i __ r..(l..(numbers)):
        numbers[i] = round(numbers[i] * n_multiply_lookup[n])
        __ l..(s..(numbers[i])) > n:
            __ numbers[i] > 0:
                numbers[i] = i..(s..(numbers[i])[:n])
            ____:
                numbers[i] = i..(s..(numbers[i])[:n +1])

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