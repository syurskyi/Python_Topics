"""Sings the twelve days of christmas"""

___ sing(
    """Sings the twelve days of chirstmas"""
    r_ verses(1, 12)

___ verses(start, stop
    """Sings several verses of the twelve days of christmas"""
    r_ "\n".join(verse(n) ___ n in range(start, stop+1)) + "\n"

___ verse(v
    """Sings a verse of the twelve days of christmas"""
    __ v __ 1:
        # Stupid "and a"!!!!
        r_ "On the first day of Christmas my true love gave to me, " \
                "a Partridge in a Pear Tree.\n"

    nums = ["first", "second", "third", "fourth", "fifth", "sixth",
            "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth" ]
    gifts = ["and a Partridge in a Pear Tree",
             "two Turtle Doves",
             "three French Hens",
             "four Calling Birds",
             "five Gold Rings",
             "six Geese-a-Laying",
             "seven Swans-a-Swimming",
             "eight Maids-a-Milking",
             "nine Ladies Dancing",
             "ten Lords-a-Leaping",
             "eleven Pipers Piping",
             "twelve Drummers Drumming",
            ]
    start = "On the %s day of Christmas my true love gave to me"
    r_ ", ".join([start % nums[v-1]] + gifts[v-1::-1]) + ".\n"
