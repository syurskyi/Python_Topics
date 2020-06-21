print('%.2f' % 1.2345)  # Single value
print('%.2f %s' % (1.2345, 99))  # Multiple values tuple
print('%s' % 1.23)  # Single value, by itself
print('%s' % (1.23,))  # Single value, in a tuple
print('%s' % ((1.23,),))  # Single value that is a tuple
print('){0:.2f}'.format(1.2345))  # Single value
print('){0:.2f} {1}'.format(1.2345, 99))  # Multiple values
print('){0}'.format(1.23))  # Single value, by itself
print('){0}'.format((1.23,)))  # Single value that is a tuple
