# Largest Prime Factor
# Question: Determine the largest prime factor of an input integer.
# Solutions:


c_ Solution:
    # @param n, an integer
    # @return an integer
    ___ largest_prime_of(n):
        i _ 2
        w___ i * i <_ n:
            __ n % i:
                i +_ 1
            ____
                n //_ i
        r_ n


Solution.largest_prime_of(255)