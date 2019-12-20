# -*- coding: utf-8 -*-

arr = ["word1", "word2", "word3"]
print(" — ".join(arr))
# 'word1 — word2 — word3'


arr = ["word1", "word2", "word3", 2]
# " — ".join(arr)
# Traceback (most recent call last):
#   File "<pyshell#69>", line 1, in <module>
#     " — ".join(arr)
# TypeError: sequence item 3: expected str instance, int found


arr = ["word1", "word2", "word3", 2]
print(" — ".join(( str(i) for i in arr )))
# 'word1 — word2 — word3 — 2'


arr = ["word1", "word2", "word3", 2]
print(str(arr))
"['word1', 'word2', 'word3', 2]"
