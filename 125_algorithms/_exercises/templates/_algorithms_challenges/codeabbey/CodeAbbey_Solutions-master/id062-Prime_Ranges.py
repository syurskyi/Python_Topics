# Python 3.4
___ gen_primes(a, limit
    primes    # list

    # Sieve of Eratosthenes
    sieve  [T..] * (limit + 1)
    ___ num __ r..(2, limit + 1
        __ num < a:
            p..
        __ sieve[num]:
           __ num > a:
               primes.a..(num)
           ___ i __ r..(num * num, limit + 1, num
               sieve[i]  F..
    r.. primes

___ primes_between
  searches  i..(input
  answer    # list
  ___ s.. __ r..(searches
    a, b  input().s.. 
    a, b  i..(a), i..(b)
    primes  gen_primes(a, b)
    count  l..(s..(primes).s..
    answer.a..(s..(count
  print(' '.j..(answer
primes_between()
