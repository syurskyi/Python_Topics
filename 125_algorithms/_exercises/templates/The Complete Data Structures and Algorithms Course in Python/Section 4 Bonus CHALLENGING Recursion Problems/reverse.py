#   Created by Elshad Karimov 
#   Copyright © AppMillers. All rights reserved.

# reverse Solution


___ reverse(strng
    __ le_(strng) <= 1:
      r_ strng
    r_ strng[le_(strng)-1] + reverse(strng[0:le_(strng)-1])


print(reverse('python')) # 'nohtyp'
print(reverse('appmillers')) # 'srellimppa'