___ dec_to_base(number, base):
    """
    Input: number is the number to be converted
           base is the new base  (eg. 2, 6, or 8)
    Output: the converted number in the new base without the prefix (eg. '0b')
    """
    # your code
    
    ___ dec_to_base_helper(number,base,x=0):
    # return n
        __ not number:
            return 0
        

        remainder = number % base

        
        return dec_to_base_helper(number//base,base,x +1) + remainder *10**x


    
    return dec_to_base_helper(number,base)


