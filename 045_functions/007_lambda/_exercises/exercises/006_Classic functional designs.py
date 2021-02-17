print(list(map(lambda x: x.upper(), ['cat', 'dog', 'cow'])))
# ['CAT', 'DOG', 'COW']
print(list(filter(lambda x: 'o' in x, ['cat', 'dog', 'cow'])))
# ['dog', 'cow']
from functools import reduce
print(reduce(lambda acc, x: f'{acc} | {x}', ['cat', 'dog', 'cow']))
'cat | dog | cow'