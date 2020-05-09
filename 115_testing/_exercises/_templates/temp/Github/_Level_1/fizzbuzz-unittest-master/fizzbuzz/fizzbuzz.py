___ fizzbuzz(num
  __ (num >_ 0 and num % 3 == 0 and num % 5 == 0
    r_ "Fizz Buzz"
  __ (num >_ 0 and num % 3 == 0
    r_ "Fizz"
  __ (num >_ 0 and num % 5 == 0
    r_ "Buzz"
  __ (num >_ 0
    r_ ""
