captains = ['Janeway', 'Picard', 'Sisko']

for captain in captains:
    print(captain)

# Janeway
# Picard
# Sisko

numbers_divisible_by_three = [3, 6, 9, 12, 15]

for num in numbers_divisible_by_three:
    quotient = num / 3
    print(f"{num} divided by 3 is {int(quotient)}.")

# 3 divided by 3 is 1.
# 6 divided by 3 is 2.
# 9 divided by 3 is 3.
# 12 divided by 3 is 4.
# 15 divided by 3 is 5.

for i in range(3, 16, 3):
    quotient = i / 3
    print(f"{i} divided by 3 is {int(quotient)}.")



captains = ['Janeway', 'Picard', 'Sisko']

for i in range(len(captains)):
    print(captains[i])

# Incrementing With range()

for i in range(3, 100, 25):
    print(i)

# 3
# 28
# 53
# 78

# Decrementing With range()

for i in range(10, -6, -2):
    print(i)

# 10
# 8
# 6
# 4
# 2
# 0
# -2
# -4

for i in reversed(range(5)):
    print(i)
