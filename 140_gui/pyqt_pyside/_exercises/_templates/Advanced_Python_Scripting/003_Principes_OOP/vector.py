c_ vector(
    ___  -  , x=0.0, y=0.0, z=0.0
        x = float(x)
        y = float(y)
        z = float(z)

    ___ __repr__ 
        return 'Vector<%0.3f, %0.3f, %0.3f>'%(x, y, z)

    ___ __str__ 
        return __repr__()

    ___ __add__ , other
        __ isinstance(other, vector
            return vector(x+other.x,
                          y+other.y,
                          z+other.z)
        else:
            raise Exception("Not supported type %s" % type(other))

    ___ __sub__ , other
        __ isinstance(other, vector
            return vector(x-other.x,
                          y-other.y,
                          z-other.z)
        else:
            raise Exception("Not supported type %s" % type(other))

    ___ __mul__ , other
        __ isinstance(other, int) or isinstance(other, float
            return vector(x * other, y * other, z * other)
        elif isinstance( other, vector
            return vector(x * other.x, y * other.y, z * other.z)

    ___ __call__ 
        return (x, y, z)

    ___ __getitem__ , item
        __ isinstance(item, int
            __ 0 <= item <=2:
                __ item __ 0:
                    return x
                elif item __ 1:
                    return y
                elif item __ 2:
                    return z
            else:
                raise Exception('Value out of range, use 0, 1 or 2')
        else:
            raise Exception('Index value mast be int')

    ___ __setitem__ , key, value
        __ isinstance(key, int
            __ key in [0,1,2]:
                __ key __ 0:
                    x = value
                elif key __ 1:
                    y = value
                elif key __ 2:
                    z = value
            else:
                raise Exception('Value out of range, use 0, 1 or 2')
        else:
            raise Exception('Index value mast be int')

    ___ __len__ 
        return int(mag())

    ___ cross , other
        __ isinstance(other, vector
            return vector(y*other.z - z*other.y,
                 z*other.x - x*other.z,
                 x*other.y - y*other.x)
        raise Exception("Not supported type %s" % type(other))

    ___ dot , other
        return x * other.x + y * other.y + z * other.z

    ___ mag 
        return (x**2 + y**2 + z**2)**0.5

a = vector()
print(a)