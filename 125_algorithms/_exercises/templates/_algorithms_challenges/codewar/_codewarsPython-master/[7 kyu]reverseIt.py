___ reverse_it(data
    __ isinstance(data,bool
        r_ data
    ____ isinstance(data,int
        r_ int(str(data)[::-1])
    ____ isinstance(data,str
        r_ data[::-1]
    ____ isinstance(data,float
        r_ float(str(data)[::-1])

    ____
        r_ data

    