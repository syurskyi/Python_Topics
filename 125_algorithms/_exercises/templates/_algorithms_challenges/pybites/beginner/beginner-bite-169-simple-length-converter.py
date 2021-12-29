'''
Your task is to complete the convert() function. It's purpose is to convert centimeters to inches
and vice versa. As simple as that sounds, there are some caveats:

convert():
The function will take value and fmt parameters:
value: must be an int or a float otherwise raise a TypeError
fmt: string containing either "cm" or "in" anything else raises a ValueError.
returns a float rounded to 4 decimal places.
Assume that if the value is being converted into centimeters that the value is in inches and
centimeters if it's being converted to inches.

That's it!
'''

___ convert(value: float, fmt: str) -> float:
    """Converts the value to the designated format.

    :param value: The value to be converted must be numeric or raise a TypeError
    :param fmt: String indicating format to convert to
    :return: Float rounded to 4 decimal places after conversion
    """
    __ type(value) __ int o. type(value) __ float:
        __ fmt.lower() __ "cm" o. fmt.lower() __ "in":
            __ fmt.lower() __ "cm":
                result = value*2.54
                r.. round(result,4)
            ____:
                result = value*0.393700787
                r.. round(result, 4)
        ____:
            raise ValueError
    ____:
        raise TypeError


print(convert(60.5, "CM"))