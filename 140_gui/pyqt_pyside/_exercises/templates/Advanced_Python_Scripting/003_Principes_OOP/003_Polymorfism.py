class vectorClass(object):
	def __init__(self, x=0, y=0, z=0):
		self.x = x
		self.y = y
		self.z = z

	def __mul__(self, other):
		if isinstance(other, (int, float)):
			return vectorClass(self.x * other,
			                  self.y * other,
			                  self.z * other)

		elif isinstance(other, vectorClass):
			return vectorClass(
				self.x * other.x,
				self.y * other.y,
				self.z * other.z)

	def __repr__(self):
		return('Vector < %s:%s:%s >' % (self.x,
		                                self.y,
		                                self.z))


v1 = vectorClass(1, 2, 3)
v2 = vectorClass(2, 3, 4)
v3 = v1 * v2
print(v3.x, v3.y, v3.z)
print(v1)
v1

