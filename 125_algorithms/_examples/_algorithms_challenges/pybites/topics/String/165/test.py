
f = open("passwd", "r")

#print(f.read().split('\n'))

lines = f.readlines()

#print(lines.split(':')[-1])

print( [line.split(':')[0] for line in lines if 'false' in line.split(':')[-1] ] )