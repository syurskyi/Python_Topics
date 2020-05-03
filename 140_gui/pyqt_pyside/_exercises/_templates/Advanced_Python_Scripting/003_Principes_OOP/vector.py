c_ vector(
    ___  -  , x_0.0, y_0.0, z_0.0
        x _ fl..(x)
        y _ fl..(y)
        z _ fl..(z)

    ___ __repr__ 
        r_ 'Vector<%0.3f, %0.3f, %0.3f>'%(x, y, z)

    ___ __str__ 
        r_ __repr__

    ___ __add__ , other
        __ isinstance(other, vector
            r_ vector(x+other.x,
                          y+other.y,
                          z+other.z)
        ____
            raise Exception("Not supported type %s" % ty..(other))

    ___ __sub__ , other
        __ isinstance(other, vector
            r_ vector(x-other.x,
                          y-other.y,
                          z-other.z)
        ____
            raise Exception("Not supported type %s" % ty..(other))

    ___ __mul__ , other
        __ isinstance(other, int) or isinstance(other, fl..
            r_ vector(x * other, y * other, z * other)
        ____ isinstance( other, vector
            r_ vector(x * other.x, y * other.y, z * other.z)

    ___ __call__ 
        r_ (x, y, z)

    ___ __getitem__ , item
        __ isinstance(item, int
            __ 0 <_ item <_2:
                __ item __ 0:
                    r_ x
                ____ item __ 1:
                    r_ y
                ____ item __ 2:
                    r_ z
            ____
                raise Exception('Value out of range, use 0, 1 or 2')
        ____
            raise Exception('Index value mast be int')

    ___ __setitem__ , key, value
        __ isinstance(key, int
            __ key __ [0,1,2]:
                __ key __ 0:
                    x _ value
                ____ key __ 1:
                    y _ value
                ____ key __ 2:
                    z _ value
            ____
                raise Exception('Value out of range, use 0, 1 or 2')
        ____
            raise Exception('Index value mast be int')

    ___ __len__ 
        r_ int(mag())

    ___ cross , other
        __ isinstance(other, vector
            r_ vector(y*other.z - z*other.y,
                 z*other.x - x*other.z,
                 x*other.y - y*other.x)
        raise Exception("Not supported type %s" % ty..(other))

    ___ dot , other
        r_ x * other.x + y * other.y + z * other.z

    ___ mag 
        r_ (x**2 + y**2 + z**2)**0.5

a _ vector
print(a)