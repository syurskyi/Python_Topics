
___ fizzbuzz(n, additional_rules_N..
    """     
    >>> fizzbuzz(2)
    '2'
    >>> fizzbuzz(3)
    'Fizz'
    >>> fizzbuzz(15)
    'FizzBuzz'
    >>> fizzbuzz(35, {7: "Whizz"})
    'BuzzWhizz'
    """
    answer _ ""
    rules _ {3: "Fizz", 5: "Buzz"}
    if additional_rules:
        rules.update(additional_rules)
    for divisor in sorted(rules.keys()):
     if n % divisor == 0:
         answer +_ rules[divisor]
    if not answer:
     answer _ st.(n)
    r_ answer
