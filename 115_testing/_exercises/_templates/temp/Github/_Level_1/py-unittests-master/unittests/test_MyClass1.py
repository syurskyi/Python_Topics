______ u__
____ src.exampleCode1 ______ MyClass1


c_ TestMyClass1?.?

    ___ test_constructor1
        obj _ MyClass1()
        aE..(obj.a, 0)
        aE..(obj.b, 1)
        aE..(obj.c, 2)

    ___ test_constructor2
        obj _ MyClass1(b_4.5, c_8)
        aE..(obj.a, 0)
        aE..(obj.b, 4.5)
        aE..(obj.c, 8)

    ___ test_product1
        obj _ MyClass1(1, 2, 3)
        aE..(obj.getProduct(), 6)

    ___ test_min1
        obj _ MyClass1(2, 2, 2)
        aE..(obj.getMin(), 2)

    ___ test_min2
        obj _ MyClass1(-10, 2, 3)
        aE..(obj.getMin(), -10)

    ___ test_max1
        obj _ MyClass1(1, 2, 3)
        aE..(obj.getMax(), 3)

    ___ test_sum1
        obj _ MyClass1(-1, 1, 0)
        aE..(obj.getSum(), 0)

    ___ test_sum2
        obj _ MyClass1(10, 20, 30)
        aE..(obj.getSum(), 60)

    ___ test_mean1
        obj _ MyClass1(10, 10, 10)
        aE..(obj.getMean(), 10)


__ __name__ __ '__main__':
    ?.?
