# Generating evens using a list comprehension:


def generate_evens():
    return [x for x in range(1,50) if x%2 == 0]

# Generating evens using a loop:


def generate_evens():
    result = []
    for x in range(1,50):
        if x % 2 == 0:
            result.append(x)
    return result