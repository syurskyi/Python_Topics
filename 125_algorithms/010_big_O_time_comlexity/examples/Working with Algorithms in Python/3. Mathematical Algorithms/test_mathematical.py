# test mathematical algorithms

from mathematical import *

a__(8192 == exponent(2,13))
a__(268435456 == exponent(4,14))
a__(1 == exponent(10,0))

a__(8192 == exponent_nonr(2,13))
a__(268435456 == exponent_nonr(4,14))
a__(1 == exponent_nonr(10,0))

a__(950 == exponent_mod(3,7,1237))

# Try number of exponentiations
m = numpy.array([1,3,1,3]).reshape((2,2))

# can't go too high b/c math overflow
for e in range(16):
    base = numpy.identity(2)
    for b in range(e):
        base = base.dot(m)
    
    m_exp = exponent_mat(m,e)

    # compare
    for Ri,Rj in zip(base,m_exp):
        for Ci,Cj in zip(Ri,Rj):
            a__(Ci == Cj)
