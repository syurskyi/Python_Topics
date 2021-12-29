def sum_numbers(numbers=None):
    total = 0
    if numbers == None:
        for i in range(1,101):
            total = total + i
    elif len(numbers) == 0:
        total = 0
    elif isinstance(numbers, list) or isinstance(numbers, tuple):
        for i in numbers:
            total = total + i
    elif not isinstance(numbers, list) or not isinstance(numbers, tuple):
        count = len(numbers)
        for i in range(0,count):
            total = total + numbers[i]
    return total