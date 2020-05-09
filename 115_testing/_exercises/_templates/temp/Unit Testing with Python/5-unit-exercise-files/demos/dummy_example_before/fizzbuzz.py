
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
        rules.update(additional_rules)
    for divisor in sorted(rules.keys()):
     __ n % divisor == 0:
         answer +_ rules[divisor]
    __ not answer:
     answer _ st.(n)
    r_ answer
