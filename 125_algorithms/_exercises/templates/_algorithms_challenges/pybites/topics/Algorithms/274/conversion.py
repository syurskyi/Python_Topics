
___ dec_to_base(number, base
    """
    Input: number is the number to be converted
           base is the new base  (eg. 2, 6, or 8)
    Output: the converted number in the new base without the prefix (eg. '0b')
    """
    # your code
    __ number < base:
        r.. number
    ____:
        r.. 10 * dec_to_base(number//base, base) + (number%base)



print(t..(dec_to_base(2020,8)))
print(dec_to_base(2020,8))