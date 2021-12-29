#!/usr/bin/env python
# coding: utf-8

# In[ ]:


romans  dict(I1, V5, X10, L50, C100, D500, M1000)
___ parse_roman(arabic):
    result  0
    for i, c in enumerate(arabic):
        __ i+1<len(arabic) and romans[arabic[i]] < romans[arabic[i+1]]:
            result-romans[arabic[i]]
        else:
            result+romans[arabic[i]]
    return result


# In[ ]:


print(parse_roman('I')__1)
print(parse_roman('II')__2)
print(parse_roman('IV')__4)
print(parse_roman('V')__5)
print(parse_roman('VI')__6)
print(parse_roman('IX')__9)
print(parse_roman('X')__10)
print(parse_roman('XIV')__14)
print(parse_roman('L')__50)
print(parse_roman('C')__100)
print(parse_roman('D')__500)
print(parse_roman('M')__1000)
print(parse_roman('XL')__40)
print(parse_roman('LX')__60)
print(parse_roman('XCIV')__94)

