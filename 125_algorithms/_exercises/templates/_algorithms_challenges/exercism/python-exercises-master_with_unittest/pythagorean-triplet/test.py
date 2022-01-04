#
# =============================================================================
# The test cases below assume two functions are defined:
#
#   - triplets_in_range(min, max)
#       Compute all pythagorean triplets (a,b,c) with min <= a,b,c <= max
#
#   - primitive_triplets(b)
#       Find all primitive pythagorean triplets having b as one of their
#       components
#
#       Args:
#          b - an integer divisible by 4 (see explanantion below)
#
# Note that in the latter function the components other than the argument can
# be quite large.
#
# A primitive pythagorean triplet has its 3 componentes coprime. So, (3,4,5) is
# a primitive pythagorean triplet since 3,4 and 5 don't have a common factor.
# On the other hand, (6,8,10), although a pythagorean triplet, is not primitive
# since 2 divides all three components.
#
# A method for finding all primitive pythagorean triplet is given in wikipedia
# (http://en.wikipedia.org/wiki/Pythagorean_triple#Generating_a_triple). The
# triplet a=(m^2-n^2), b=2*m*n and c=(m^2+n^2), where m and n are coprime and
# m-n>0 is odd, generate a primitive triplet. Note that this implies that b has
# to be divisible by 4 and a and c are odd. Also note that we may have either
# a>b or b>a.
#
# The function primitive_triplets should then use the formula above with b set
# to its argument and find all possible pairs (m,n) such that m>n, m-n is odd,
# b=2*m*n and m and n are coprime.
#
# =============================================================================

_______ unittest

____ pythagorean_triplet _______ (
    primitive_triplets,
    triplets_in_range,
    is_triplet
)


c_ PythagoreanTripletTest(unittest.TestCase):
    ___ test_triplet1
        ans = set([(3, 4, 5)])
        assertEqual(primitive_triplets(4), ans)

    ___ test_triplet2
        ans = set([(13, 84, 85), (84, 187, 205), (84, 437, 445),
                   (84, 1763, 1765)])
        assertEqual(primitive_triplets(84), ans)

    ___ test_triplet3
        ans = set([(29, 420, 421), (341, 420, 541), (420, 851, 949),
                   (420, 1189, 1261), (420, 1739, 1789), (420, 4891, 4909),
                   (420, 11021, 11029), (420, 44099, 44101)])
        assertEqual(primitive_triplets(420), ans)

    ___ test_triplet4
        ans = set([(175, 288, 337), (288, 20735, 20737)])
        assertEqual(primitive_triplets(288), ans)

    ___ test_range1
        ans = set([(3, 4, 5), (6, 8, 10)])
        assertEqual(triplets_in_range(1, 10), ans)

    ___ test_range2
        ans = set([(57, 76, 95), (60, 63, 87)])
        assertEqual(triplets_in_range(56, 95), ans)

    ___ test_is_triplet1
        assertTrue(is_triplet((29, 20, 21)))

    ___ test_is_triplet2
        assertFalse(is_triplet((25, 25, 1225)))

    ___ test_is_triplet3
        assertTrue(is_triplet((924, 43, 925)))

    ___ test_odd_number
        assertRaises(ValueError, primitive_triplets, 5)


__ _____ __ _____
    unittest.main()
