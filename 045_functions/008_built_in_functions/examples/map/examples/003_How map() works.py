def calculateSquare(n):
  return n*n

numbers = (1, 2, 3, 4)
result = map(calculateSquare, numbers)
print(result)

# converting map object to set
numbersSquare = set(result)
print(numbersSquare)

# <map object at 0x7f722da129e8>
# {16, 1, 4, 9}

