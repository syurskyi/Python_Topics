# Counter
# это подкласс dict, предназначенный для подсчёта хешируемых объектов.  Также его иногда называют мультимножеством.
# Элементы сохраняются как ключи словаря, а их количество -- как значения.

# подсчитать количество каждого символа в строке using Counter
from collections import Counter
c = Counter('abcdeabcdabcaba')

# три наиболее частых элемента
# using Counter
from collections import Counter
c = Counter('abcdeabcdabcaba')
print(c.most_common(3))

# все уникальные элементы
# using Counter
from collections import Counter
c = Counter('abcdeabcdabcaba')
print(sorted(c))

# все элементы
# using Counter
from collections import Counter
c = Counter('abcdeabcdabcaba')
print(sorted(c.elements()))

# сумма значений
# using Counter
from collections import Counter
c = Counter('abcdeabcdabcaba')
print(sum(c.values()))

# количество букв 'a'
# using Counter
from collections import Counter
c = Counter('abcdeabcdabcaba')
print(c['a'])

# добавить новые буквы
# using Counter
from collections import Counter
c = Counter('abcdeabcdabcaba')
for elem in 'shazam':
    c[elem] += 1

# удалить все 'b'
# using Counter
from collections import Counter
c = Counter('abcdeabcdabcaba')
del c['b']

# создать новый счётчик
# using Counter
from collections import Counter
d = Counter('simsalabim')

# добавить его элементы в первый
# using Counter
from collections import Counter
c = Counter('abcdeabcdabcaba')
d = Counter('simsalabim')
c.update(d)

# очистить счётчик
# using Counter
from collections import Counter
c = Counter('abcdeabcdabcaba')
c.clear()

# # внимание: если счёт элемента установить или уменьшить до нуля, он останется в
# # счётчике, пока не будет удалён явно
# using Counter
c = Counter('aaabbc')
c['b'] -= 2
print(c.most_common())

