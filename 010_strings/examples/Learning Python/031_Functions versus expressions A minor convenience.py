# def myformat(fmt, args): return fmt % args # See Part IV
# myformat('%s %s', (88, 99)) # Call your function object
# str.format('{} {}', 88, 99) # Versus calling the built-in
# otherfunction(myformat) # Your function is an object too

print('%(num)i = %(title)s' % dict(num=7, title='Strings'))
print('{num:d} = {title:s}'.format(num=7, title='Strings'))
print('{num} = {title}'.format(**dict(num=7, title='Strings')))
import string
t = string.Template('$num = $title')
print(t.substitute({'num': 7, 'title': 'Strings'}))
print(t.substitute(num=7, title='Strings'))
print(t.substitute(dict(num=7, title='Strings')))


