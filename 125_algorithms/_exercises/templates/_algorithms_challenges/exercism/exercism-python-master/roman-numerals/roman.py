"""Converts integers to roman numerals"""

# Map of integers to roman numberal digits
DIGITS = {1:  "I",
          4:  "IV",
          5:  "V",
          9:  "IX",
          10: "X",
          40: "XL",
          50: "L",
          90: "XC",
          100:"C",
          400:"CD",
          500:"D",
          900:"CM",
          1000:"M",
         }


___ numeral(num
    """Converts integers to roman numberals"""
    roman = ""
    ___ digit __ reversed(sorted(DIGITS.keys())):
        roman += DIGITS[digit] * (num // digit)
        num %= digit
    r_ roman
