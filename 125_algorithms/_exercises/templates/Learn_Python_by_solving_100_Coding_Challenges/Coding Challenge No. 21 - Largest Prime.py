# Largest Prime Factor
# Question: Determine the largest prime factor of an input integer.
# Solutions:


class Solution:
    # @param n, an integer
    # @return an integer
    def largest_prime_of(n):
        i = 2
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
        return n


Solution.largest_prime_of(255)