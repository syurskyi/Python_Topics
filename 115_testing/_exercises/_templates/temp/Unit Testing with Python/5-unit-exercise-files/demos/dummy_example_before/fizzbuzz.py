
___ fizzbuzz(n, additional_rules
    """     
    >>> fizzbuzz(2, None)
    '2'
    >>> fizzbuzz(3, None)
    'Fizz'
    >>> fizzbuzz(15, None)
    'FizzBuzz'
    >>> fizzbuzz(35, {7: "Whizz"})
    'BuzzWhizz'
    """
    answer _ ""
    rules _ {3: "Fizz", 5: "Buzz"}
    __ additional_rules:
        rules.u..(additional_rules)
    ___ divisor __ sorted(rules.keys()):
     __ n % divisor __ 0:
         answer +_ rules[divisor]
    __ no. answer:
     answer _ st.(n)
    r_ answer
