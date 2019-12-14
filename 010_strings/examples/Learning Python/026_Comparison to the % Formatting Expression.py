import sys
print('#' * 52 + ' Format expression: in all 2.X/3.X')
print('%s=%s' % ('spam', 42))  # Format expression: in all 2.X/3.X

print('#' * 52 + ' Format method: in 3.0+ and 2.6+')
print('{0}={1}'.format('spam', 42))  # Format method: in 3.0+ and 2.6+

print('#' * 52 + ' With autonumbering: in 3.1+ and 2.7')
print('{}={}'.format('spam', 42))  # With autonumbering: in 3.1+ and 2.7

print('#' * 52 + ' Arbitrary types')
print('%s, %s and %s' % (3.14, 42, [1, 2]))  # Arbitrary types
print('My %(kind)s runs %(platform)s' % {'kind': 'laptop', 'platform': sys.platform})
print('My %(kind)s runs %(platform)s' % dict(kind='laptop', platform=sys.platform))
somelist = list('SPAM')
parts = somelist[0], somelist[-1], somelist[1:3]
print('first=%s, last=%s, middle=%s' % parts)


# Adding specific formatting
print('#' * 52 + ' Adding specific formatting')
print('%-10s = %10s' % ('spam', 123.4567))
print('%10s = %-10s' % ('spam', 123.4567))
print('%(plat)10s = %(kind)-10s' % dict(plat=sys.platform, kind='laptop'))

# Floating-point numbers
print('#' * 52 + ' Floating-point numbers')
print('%e, %.3e, %g' % (3.14159, 3.14159, 3.14159))
print('%f, %.2f, %06.2f' % (3.14159, 3.14159, 3.14159))

# Hex and octal, but not binary (see ahead)
print('#' * 52 + ' Hex and octal, but not binary (see ahead)')
print('%x, %o' % (255, 255))

# Hardcoded references in both
print('#' * 52 + ' Hardcoded references in both')
import sys
print('My {1[kind]:<8} runs {0.platform:>8}'.format(sys, {'kind': 'laptop'}))
print('My %(kind)-8s runs %(plat)8s' % dict(kind='laptop', plat=sys.platform))

# Building data ahead of time in both
print('#' * 52 + ' Building data ahead of time in both')
data = dict(platform=sys.platform, kind='laptop')
print('My {kind:<8} runs {platform:>8}'.format(**data))
print('My %(kind)-8s runs %(platform)8s' % data)
print('{0:d}'.format(999999999999))
print('{0:,d}'.format(999999999999))
print('{:,d}'.format(999999999999))
print('{:,d} {:,d}'.format(9999999, 8888888))
print('{:,.2f}'.format(296999.2567))
from formats import commas, money
print('%s' % commas(999999999999))
print('%s %s' % (commas(9999999), commas(8888888)))
print('%s' % money(296999.2567))
print([commas(x) for x in (9999999, 8888888)])
print('%s %s' % tuple(commas(x) for x in (9999999, 8888888)))
print(''.join(commas(x) for x in (9999999, 8888888)))
