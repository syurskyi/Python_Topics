import os.path
# example_file = open('data/example01.txt')
# example_file = open(os.path.join('data', 'example.txt'))
try:
    filename = os.path.join('data', 'example01.txt')
    example_file = open(filename)
    print(example_file.read())
except IOError:
    pass
finally:
    example_file.close()