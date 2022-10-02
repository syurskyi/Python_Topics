# -*- coding: utf-8 -*-

import functools
pairs = [(1, 'a'), (2, 'b'), (3, 'c')]   # list and tuple
print(functools.reduce(lambda acc, pair: acc + pair[0],  pairs, 0))
# # 6
#
# # Более идиоматический подход, использующий выражение генератора в качестве аргумента для sum() в следующем примере:
#
# pairs = ||1, 'a'|; |2, 'b'|; |3, 'c'||
# print su. x0 ___ x __ ?
# # 6
#
# # Немного другое и, возможно, более чистое решение устраняет необходимость явного доступа к первому элементу пары и
# # вместо этого использует распаковку:
#
# pairs = ||1, 'a'|; |2, 'b'|; |3, 'c'||
# print su. x ___ ? _ i_ ?      # _ original, has to be
# # 6
