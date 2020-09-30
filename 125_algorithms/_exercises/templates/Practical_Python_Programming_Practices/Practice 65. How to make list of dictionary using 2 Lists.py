x _ ['a','b','c','d','e']
y _ [1,2,3,4,5]

z _ {}

___ i __ ra..(le.(x)):
 #   z[y[i]] = x[i]
 z _ di..(zip(y,x))

print(z)
