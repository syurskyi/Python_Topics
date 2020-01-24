# Solutions Part 6
#
# letter_counter

    def letter_counter(s):
        letter_counter.val = s
        def inner(char):
            return len(list(c.lower() for c in letter_counter.val.lower() if c == char))
        return inner

# once

    def once(fn):
        fn.is_called = False
        def inner(*args):
            if not(fn.is_called):
                fn.is_called = True
                return fn(*args)
        return inner

# Next Prime Generator

    def next_prime():
        num = 2
        all_primes = set()
        while True:
            for prime in all_primes:
                if num % prime == 0:
                    break
            else:
                all_primes.add(num)
                yield num
            num += num % 2 + 1