# -*- coding: utf-8 -*-

import re
p = re.compile(r"[\s,.]+")
p.split("word1, word2\nword3\r\nword4.word5")
# ['word1', 'word2', 'word3', 'word4', 'word5']
p.split("word1, word2\nword3\r\nword4.word5", 2)
# ['word1', 'word2', 'word3\r\nword4.word5']


p = re.compile(r"[0-9]+")
p.split("word, word\nword")
# ['word, word\nword']


p = re.compile(r"[\s,.]+")
re.split(p, "word1, word2\nword3")
# ['word1', 'word2', 'word3']
re.split(r"[\s,.]+", "word1, word2\nword3")
# ['word1', 'word2', 'word3']

print(re.escape(r"[]().*"))
# \[\]\(\)\.\*

re.purge()