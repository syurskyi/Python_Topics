# -*- coding: utf-8 -*-

_______ __
p _ __.c..(r"[\s,.]+")
p.s..("word1, word2\nword3\r\nword4.word5")
# ['word1', 'word2', 'word3', 'word4', 'word5']
p.s..("word1, word2\nword3\r\nword4.word5", 2)
# ['word1', 'word2', 'word3\r\nword4.word5']


p _ __.c..(r"[0-9]+")
p.s..("word, word\nword")
# ['word, word\nword']


p _ __.c..(r"[\s,.]+")
__.s..(p, "word1, word2\nword3")
# ['word1', 'word2', 'word3']
__.s..(r"[\s,.]+", "word1, word2\nword3")
# ['word1', 'word2', 'word3']

print(__.escape(r"[]().*"))
# \[\]\(\)\.\*

__.purge()
