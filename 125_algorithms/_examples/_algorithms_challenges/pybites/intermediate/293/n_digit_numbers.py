from typing import List, TypeVar
T = TypeVar('T', int, float)


def n_digit_numbers(numbers: List[T], n: int) -> List[int]:
    # Checks
    if n < 1:
        raise ValueError

    if numbers == []:
        return []

    n_multiply_lookup = {1: 1, 2: 10, 3: 100, 4: 1000}

    for i in range(len(numbers)):
        numbers[i] = round(numbers[i] * n_multiply_lookup[n])
        if len(str(numbers[i])) > n:
            if numbers[i] > 0:
                numbers[i] = int(str(numbers[i])[:n])
            else:
                numbers[i] = int(str(numbers[i])[:n +1])

    return numbers

#if __name__ == "__main__":
    #print(n_digit_numbers([], 2))
    #print(n_digit_numbers([1, 2, 3], 1))
    #print(n_digit_numbers([1, 2, 3], 2))
    #print(n_digit_numbers([0, 1, 2, 3], 2))
    #print(n_digit_numbers([8, 9, 10], 2))
    #print(n_digit_numbers([5.2, 1600, 520, 3600, 13, 55, 4000], 2))
    #print(n_digit_numbers([-1.1, 2.22, -3.333], 3))
    #print(n_digit_numbers([-1.1, 2.22, -3.333, 4444, 55555], 4))