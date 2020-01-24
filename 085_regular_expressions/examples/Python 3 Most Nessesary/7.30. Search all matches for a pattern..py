# -*- coding: utf-8 -*-

import re
p = re.compile(r"[0-9]+")
p.findall("2007, 2008, 2009, 2010, 2011")
# ['2007', '2008', '2009', '2010', '2011']
p = re.compile(r"[a-z]+")
p.findall("2007, 2008, 2009, 2010, 2011")
# []
t = r"(([0-9]{3})-([0-9]{2})-([0-9]{2}))"
p = re.compile(t)
p.findall("322-77-20, 528-22-98")
# [('322-77-20', '322', '77', '20'),
#  ('528-22-98', '528', '22', '98')]


re.findall(r"[0-9]+", "1 2 3 4 5 6")
# ['1', '2', '3', '4', '5', '6']
p = re.compile(r"[0-9]+")
re.findall(p, "1 2 3 4 5 6")
# ['1', '2', '3', '4', '5', '6']


p = re.compile(r"[0-9]+")
for m in p.finditer("2007, 2008, 2009, 2010, 2011"):
    print(m.group(0), "start:", m.start(), "end:", m.end())

# 2007 start: 0 end: 4
# 2008 start: 6 end: 10
# 2009 start: 12 end: 16
# 2010 start: 18 end: 22
# 2011 start: 24 end: 28


p = re.compile(r"<b>(.+?)</b>", re.I | re.S)
s = "<b>Text1</b>Text2<b>Text3</b>"
for m in re.finditer(p, s):
    print(m.group(1))

# Text1
# Text3