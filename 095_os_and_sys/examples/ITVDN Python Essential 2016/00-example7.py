filename = 'data/example02.txt'

with open(filename) as data:
    lines = data.readlines()

lines.insert(1, 'inserted line\n')

with open(filename, 'w') as data:
    data.writelines(lines)