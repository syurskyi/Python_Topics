# -*- coding: utf-8 -*-

import re

s = "<b>Text1</b>Text2<I>Text3</I><b>Text4</b>"
p = re.compile(r"<([a-z]+)>(.*?)</\1>", re.S | re.I)
p.findall(s)
# [('b', 'Text1'), ('I', 'Text3'), ('b', 'Text4')]