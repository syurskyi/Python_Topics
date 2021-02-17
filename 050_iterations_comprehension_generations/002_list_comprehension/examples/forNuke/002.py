# h_letters = []
#
# for letter in 'human','Gray':
#     h_letters.append(letter)
#
# print(h_letters)

h_letters = [letter for letter in 'human' for letter in 'Gray']
print(h_letters)