# -*- coding: utf-8 -*-

import re

s = "<b>Text1</b>Text2<b>Text3</b>"
p = re.compile(r"<b>.*?</b>", re.S)
p.findall(s)
# ['<b>Text1</b>', '<b>Text3</b>']