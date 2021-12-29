# 5! = 120:
#
# 5 * 4 * 3 * 2 * 1


___ factorial(n):
    __ n __ 1:
        r.. 1

    r.. n * factorial(n - 1)


print("5!={:,}, 3!={:,}, 11!={:,}".format(
    factorial(5),  # 120
    factorial(3),  # 6
    factorial(11)  # HUGE
))


# Fibonacci numbers:
# 1, 1, 2, 3, 5, 8, 13, 21, ...

___ fibonacci(limit):
    nums  []

    current  0
    next  1

    w___ current < limit:
        current, next  next, next + current
        nums.a..(current)

    r.. nums


print('via lists')
___ n __ fibonacci(100):
    print(n, end', ')

print()


___ fibonacci_co():
    current  0
    next  1

    w___ T...
        current, next  next, next + current
        yield current


print('with yield')
___ n __ fibonacci_co():
    __ n > 1000:
        _____

    print(n, end', ')














