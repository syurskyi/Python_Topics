c_ vectorClass(object
	___  -  , x_0, y_0, z_0
		x _ x
		y _ y
		z _ z

	___ __mul__ , other
		__ isinstance(other, (int, fl..)):
			r_ vectorClass(x * other,
			                  y * other,
			                  z * other)

		____ isinstance(other, vectorClass
			r_ vectorClass(
				x * other.x,
				y * other.y,
				z * other.z)

	___ __repr__
		r_('Vector < %s:%s:%s >' % (x,
		                                y,
		                                z))


v1 _ vectorClass(1, 2, 3)
v2 _ vectorClass(2, 3, 4)
v3 _ v1 * v2
print(v3.x, v3.y, v3.z)
print(v1)
v1

