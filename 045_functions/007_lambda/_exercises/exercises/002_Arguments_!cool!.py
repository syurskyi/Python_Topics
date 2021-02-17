print(lambda x, y, z: x + y + z)(1, 2, 3)
# 6
print(lambda x, y, z=3: x + y + z)(1, 2)
# 6
print(lambda x, y, z=3: x + y + z)(1, y=2)
# 6
print(lambda *args: sum(args))(1, 2, 3)
# 6
print(lambda **kwargs: sum(kwargs.values)(one=1, two=2, three=3))
# 6
print(lambda x, *, y=0, z=0: x + y + z)(1, y=2, z=3)
# 6