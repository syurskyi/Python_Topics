# -*- coding: utf-8 -*-

html = """<html>
<head><title>%(title)s</title>
</head>
<body>
<h1>%(h1)s</h1>
<div>%(content)s</div>
</body>
</html>"""
arr = {"title":    "Это название документа",
       "h1":       "Это заголовок первого уровня",
       "content":  "Это основное содержание страницы"}
print(html % arr) # Подставляем значения и выводим шаблон
input()


s = "1\t12\t123\t"
print("'%s'" % s.expandtabs(4))
# "'1   12  123 '"


s = "\t"
print("'%s' — '%s'" % (s.expandtabs(), s.expandtabs(4)))
# "'        ' — '    '"
s = "1234\t"
print("'%s'" % s.expandtabs(4))
# "'1234    '"


s = "12345\t123456\t1234567\t1234567890\t"
print("'%s'" % s.expandtabs(4))
# "'12345   123456  1234567 1234567890  '"


s = "str"
print(s.center(15), s.center(11, "-"))
# ('      str      ', '----str----')


s = "str"
print("'%15s' '%-15s' '%s'" % (s, s, s.center(15)))
# "'            str' 'str            ' '      str      '"


s = "string"
print(s.center(6), s.center(5))
# ('string', 'string')


s = "string"
print(s.ljust(15), s.ljust(15, "-"))
# ('string         ', 'string---------')
print(s.ljust(6), s.ljust(5))
# ('string', 'string')


s = "string"
print(s.rjust(15), s.rjust(15, "-"))
# ('         string', '---------string')
print(s.rjust(6), s.rjust(5))
# ('string', 'string')

print("5".zfill(20), "123456".zfill(5))
# ('00000000000000000005', '123456')