import array
import os.path

filename = 'data/example08.bin'
filesize = os.path.getsize(filename)
count = filesize // array.array('i').itemsize
numbers = array.array('i', (0 for _ in range(count)))

with open(filename, 'rb') as binary_file:
    binary_file.readinto(numbers)

print(numbers.tolist())