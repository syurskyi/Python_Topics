def generate_power(exponent):
    def decorator(f):
        def inner(*args):
            result = f(*args)
            return exponent**result
        return inner
    return decorator


@generate_power(2)
def raise_two(n):
    return n

print(raise_two(7))


@generate_power(3)
def raise_three(n):
    return n

print(raise_two(5))
