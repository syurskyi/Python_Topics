___ filter_positive_even_numbers(numbers):
    """Receives a list of numbers, and returns a filtered list of only the
       numbers that are both positive and even (divisible by 2), try to use a
       list comprehension."""
    even_numbers = []
    for n in numbers:
        __ (n % 2 == 0) and (n > 0):
            even_numbers.append(n)
    print(even_numbers)
    pass