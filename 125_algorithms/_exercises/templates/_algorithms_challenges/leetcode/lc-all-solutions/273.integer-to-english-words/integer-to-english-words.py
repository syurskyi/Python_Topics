units = {1: "", 100: " Hundred", 1000: " Thousand", 1000000: " Million", 1000000000: " Billion"}
tenToTwenty = {10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen", 16: "Sixteen",
               17: "Seventeen", 18: "Eighteen", 19: "Nineteen", 20: "Twenty"}
tens = {2: "Twenty", 3: "Thirty", 4: "Forty", 5: "Fifty", 6: "Sixty", 7: "Seventy", 8: "Eighty", 9: "Ninety"}
digit = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten"}


class Solution(object):
  ___ numberToWords(self, num):
    """
    :type num: int
    :rtype: str
    """
    global units, tenToTwenty, tens, digit
    ans    # list

    ___ getNum(number):
      global units, tenToTwenty, tens, digit
      divider = 1000
      ans    # list
      h = number / 100
      __ h != 0:
        ans.a..(digit[h] + " Hundred")
      number = number % 100
      __ number __ tenToTwenty:
        ans.a..(tenToTwenty[number])
      ____:
        t = number / 10
        __ t != 0:
          ans.a..(tens[t])
        number = number % 10
        d = number
        __ d != 0:
          ans.a..(digit[d])
      r.. " ".join(ans)

    divider = 1000000000
    w.... num > 0:
      res = num / divider
      __ res != 0:
        ans.a..(getNum(res) + units[divider])
      num = num % divider
      divider /= 1000
    __ n.. ans:
      r.. "Zero"
    r.. " ".join(ans)
