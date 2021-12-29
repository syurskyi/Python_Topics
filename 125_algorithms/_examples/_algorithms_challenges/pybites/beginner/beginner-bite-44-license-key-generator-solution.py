import random
import string

def gen_key(parts=4, chars_per_part=8):
   par = []
   for i in range(0, parts):
      par.append(''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(chars_per_part)))
   return '-'.join(par)


print(gen_key())