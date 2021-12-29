___ is_armstrong(n: int) -> bool:
    digit_count = len(str(n))
    input_n = n
    sum = 0
    while (n != 0):
        rem = n % 10
        sum += rem ** digit_count
        n = n // 10
    return sum == input_n