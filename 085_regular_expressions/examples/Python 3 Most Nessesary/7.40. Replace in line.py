# -*- coding: utf-8 -*-

import re
p = re.compile(r"<(?P<tag1>[a-z]+)><(?P<tag2>[a-z]+)>")
p.sub(r"<\2><\1>", "<br><hr>")             # \номер
# '<hr><br>'
p.sub(r"<\g<2>><\g<1>>", "<br><hr>")       # \g<номер>
# '<hr><br>'
p.sub(r"<\g<tag2>><\g<tag1>>", "<br><hr>") # \g<название>
# '<hr><br>'


# -*- coding: utf-8 -*-
import re
def repl(m):
    """ Функция для замены. m — объект Match """
    x = int(m.group(0))
    x += 10
    return "{0}".format(x)

p = re.compile(r"[0-9]+")
# Заменяем все вхождения
print(p.sub(repl, "2008, 2009, 2010, 2011"))
# Заменяем только первые два вхождения
print(p.sub(repl, "2008, 2009, 2010, 2011", 2))
input()


# -*- coding: utf-8 -*-
import re
def repl(m):
    """ Функция для замены. m — объект Match """
    tag1 = m.group("tag1").upper()
    tag2 = m.group("tag2").upper()
    return "<{0}><{1}>".format(tag2, tag1)
p = r"<(?P<tag1>[a-z]+)><(?P<tag2>[a-z]+)>"
print(re.sub(p, repl, "<br><hr>"))
input()


p = re.compile(r"[0-9]+")
p.subn("0", "2008, 2009, 2010, 2011")
# ('0, 0, 0, 0', 4)


p = r"200[79]"
re.subn(p, "2001", "2007, 2008, 2009, 2010")
# ('2001, 2008, 2001, 2010', 2)


p = re.compile(r"<(?P<tag1>[a-z]+)><(?P<tag2>[a-z]+)>")
m = p.search("<br><hr>")
m.expand(r"<\2><\1>")             # \номер
# '<hr><br>'
m.expand(r"<\g<2>><\g<1>>")       # \g<номер>
# '<hr><br>'
m.expand(r"<\g<tag2>><\g<tag1>>") # \g<название>
# '<hr><br>'