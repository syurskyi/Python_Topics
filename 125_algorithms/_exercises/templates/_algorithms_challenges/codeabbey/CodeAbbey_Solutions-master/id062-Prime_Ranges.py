# Python 3.4
___ gen_primes(a, limit):
    primes    # list

    # Sieve of Eratosthenes
    sieve = [True] * (limit + 1)
    ___ num __ r..(2, limit + 1):
        __ num < a:
            pass
        __ sieve[num]:
           __ num >= a:
               primes.a..(num)
           ___ i __ r..(num * num, limit + 1, num):
               sieve[i] = False
    r.. primes

___ primes_between():
  searches = int(input())
  answer    # list
  ___ search __ r..(searches):
    a, b = input().s.. 
    a, b = int(a), int(b)
    primes = gen_primes(a, b)
    count = l..(str(primes).split())
    answer.a..(str(count))
  print(' '.join(answer))
primes_between()
