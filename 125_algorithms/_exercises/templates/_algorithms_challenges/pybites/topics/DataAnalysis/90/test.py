from collections import defaultdict
from typing import Counter

count = defaultdict(Counter)

count['khoo']['a'] = 1
count['khoo']['b'] = 2

#count['chuan'] += 1

#print(count['chuan'])

print(count['swee'])