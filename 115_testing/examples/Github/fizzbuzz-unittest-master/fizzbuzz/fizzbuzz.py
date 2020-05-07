def fizzbuzz(num):
  if (num >= 0 and num % 3 == 0 and num % 5 == 0):
    return "Fizz Buzz"
  if (num >= 0 and num % 3 == 0):
    return "Fizz"
  if (num >= 0 and num % 5 == 0):
    return "Buzz"
  if (num >= 0):
    return ""
