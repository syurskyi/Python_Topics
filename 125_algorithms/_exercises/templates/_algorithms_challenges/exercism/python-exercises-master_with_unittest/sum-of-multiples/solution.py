___ sum_of_multiples(limit, multiples):
    return sum(value for value in range(limit)
               __ any(value % multiple == 0
                      for multiple in multiples))
