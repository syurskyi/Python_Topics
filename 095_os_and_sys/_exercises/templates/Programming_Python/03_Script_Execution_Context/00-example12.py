# numbers = []
# with open('data/example08.txt') as text_file:
#     for line in text_file:
#         numbers.append(int(line))

with open('data/example08.txt') as text_file:
    numbers = [int(line) for line in text_file]

print(numbers)