import fizzbuzz
from fizzbuzz import fizzbuzz
import unittest

class TestFizzbuzz(unittest.TestCase):

  def test_divisible_by_only_three(self):
    data = [3, 6, 111]
    for num in data:
      self.assertEqual(fizzbuzz.fizzbuzz(num), "Fizz")

  def test_divisible_by_only_five(self):
    data = [5, 10, 110]
    for num in data:
      self.assertEqual(fizzbuzz.fizzbuzz(num), "Buzz")

  def test_divisible_by_three_and_five(self):
    data = [15, 30, 300]
    for num in data:
      self.assertEqual(fizzbuzz.fizzbuzz(num), "Fizz Buzz")

  def test_not_divisible_by_three_or_five(self):
    data = [1, 4, 109]
    for num in data:
      self.assertEqual(fizzbuzz.fizzbuzz(num), "")

if __name__ == '__main__':
  unittest.main()
