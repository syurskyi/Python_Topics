c_ vectorClass(object
	___  -  , x=0, y=0, z=0
		x = x
		y = y
		z = z

	___ __mul__ , other
		__ isinstance(other, (int, float)):
			return vectorClass(x * other,
			                  y * other,
			                  z * other)

		elif isinstance(other, vectorClass
			return vectorClass(
				x * other.x,
				y * other.y,
				z * other.z)

	___ __repr__
		return('Vector < %s:%s:%s >' % (x,
		                                y,
		                                z))


v1 = vectorClass(1, 2, 3)
v2 = vectorClass(2, 3, 4)
v3 = v1 * v2
print(v3.x, v3.y, v3.z)
print(v1)
v1

