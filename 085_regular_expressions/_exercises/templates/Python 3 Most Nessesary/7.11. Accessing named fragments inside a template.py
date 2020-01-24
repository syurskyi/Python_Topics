# -*- coding: utf-8 -*-

import re

s = "<b>Text1</b>Text2<I>Text3</I>"
p = re.compile(r"<(?P<tag>[a-z]+)>(.*?)</(?P=tag)>", re.S | re.I)
p.findall(s)
# [('b', 'Text1'), ('I', 'Text3')]


s = "text1, text2, text3 text4"
p = re.compile(r"\w+(?=[,])", re.S | re.I)
p.findall(s)
# ['text1', 'text2']


s = "text1, text2, text3 text4"
p = re.compile(r"[a-z]+[0-9](?![,])", re.S | re.I)
p.findall(s)
# ['text3', 'text4']


s = "text1, text2, text3 text4"
p = re.compile(r"(?<=[,][ ])[a-z]+[0-9]", re.S | re.I)
p.findall(s)
# ['text2', 'text3']


s = "text1, text2, text3 text4"
p = re.compile(r"(?<![,]) ([a-z]+[0-9])", re.S | re.I)
p.findall(s)
# ['text4']


s = "text1 'text2' 'text3 text4, text5"
p = re.compile(r"(')?([a-z]+[0-9])(?(1)'|,)", re.S | re.I)
p.findall(s)
# [("'", 'text2'), ('', 'text4')]


s = "-word1 -word2 -word3 -word4 -word5"
re.findall(r"\s\-([a-z0-9]+)\s", s, re.S | re.I)
# ['word2', 'word4']


re.findall(r"(?:^|\s)\-([a-z0-9]+)(?:\s|$)", s, re.S | re.I)
# ['word1', 'word3', 'word5']


re.findall(r"(?:^|\s)\-([a-z0-9]+)(?=\s|$)", s, re.S | re.I)
# ['word1', 'word2', 'word3', 'word4', 'word5']