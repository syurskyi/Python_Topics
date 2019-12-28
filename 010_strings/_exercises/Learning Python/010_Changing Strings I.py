S = 'spam'
# # S[0] = 'x' # Raises an error!
# # TypeError: 'str' object does not support item assignment
#
S = S + 'SPAM!' # To change a string, make a new one
print(S)
S = S[:4] + 'Burger' + S[-1]
print(S)


S = 'splot'
S = S.replace('pl', 'pamal')
print(S)


print('That is %d %s bird!' % (1, 'dead'))  # Format expression: all Pythons the firt is digit the second string
#
print('That is {0} {1} bird!'.format(1, 'dead'))  # Format method in 2.6, 2.7, 3.X
