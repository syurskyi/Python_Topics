# '\n%s<Class %s, address %s:\n%s%s%s>\n' % (...)  # Expression
# '\n{0}<Class {1}, address {2}:\n{3}{4}{5}>\n'.format(...)  # Method

print('The {0} side {1} {2}'.format('bright', 'of', 'life'))  # Python 3.X, 2.6+
print('The {} side {} {}'.format('bright', 'of', 'life'))  # Python 3.1+, 2.7+
print('The %s side %s %s' % ('bright', 'of', 'life'))  # All Pythons
print('{0:f}, {1:.2f}, {2:05.2f}'.format(3.14159, 3.14159, 3.14159))
print('{:f}, {:.2f}, {:06.2f}'.format(3.14159, 3.14159, 3.14159))
print('%f, %.2f, %06.2f' % (3.14159, 3.14159, 3.14159))
