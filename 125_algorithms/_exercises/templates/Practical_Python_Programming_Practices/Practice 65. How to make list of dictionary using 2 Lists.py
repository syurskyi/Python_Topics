x = ['a','b','c','d','e']
y = [1,2,3,4,5]

z = {}

___ i __ range(len(x)):
 #   z[y[i]] = x[i]
 z = dict(zip(y,x))

print(z)
