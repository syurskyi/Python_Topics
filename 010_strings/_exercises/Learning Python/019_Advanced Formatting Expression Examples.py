x = 1234
res = 'integers: ...%d...%-6d...%06d' % (x, x, x)       # | digit
print(res)
x = 1.23456789
print(x)  # Shows more digits before 2.7 and 3.1
print('%e | %f | %g' %  (x, x, x))      # |exponential | float | shot of exponential
print('%E' % x)                 # |exponential big letter
print('%-6.2f | %05.2f | %+06.1f' % (x, x, x))    # float
print('%s' % x, str(x))                # | string
print('%f, %.2f, %.*f' % (1/3.0, 1/3.0, 4, 1/3.0))   # |float
