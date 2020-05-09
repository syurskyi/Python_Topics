______ fizzbuzz
____ fizzbuzz ______ fizzbuzz
______ unittest

c_ TestFizzbuzz(unittest.TestCase):

  ___ test_divisible_by_only_three
    data _ [3, 6, 111]
    for num in data:
      assertEqual(fizzbuzz.fizzbuzz(num), "Fizz")

  ___ test_divisible_by_only_five
    data _ [5, 10, 110]
    for num in data:
      assertEqual(fizzbuzz.fizzbuzz(num), "Buzz")

  ___ test_divisible_by_three_and_five
    data _ [15, 30, 300]
    for num in data:
      assertEqual(fizzbuzz.fizzbuzz(num), "Fizz Buzz")

  ___ test_not_divisible_by_three_or_five
    data _ [1, 4, 109]
    for num in data:
      assertEqual(fizzbuzz.fizzbuzz(num), "")

if __name__ == '__main__':
  unittest.main()
