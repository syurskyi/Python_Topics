_______ unittest

____ triangle _______ Triangle, TriangleError


c_ TriangleTests(unittest.TestCase
    ___ test_equilateral_triangles_have_equal_sides
        assertEqual(Triangle(2, 2, 2).kind(), "equilateral")

    ___ test_larger_equilateral_triangles_also_have_equal_sides
        assertEqual(Triangle(10, 10, 10).kind(), "equilateral")

    ___ test_isosceles_triangles_have_last_two_sides_equal
        assertEqual(Triangle(3, 4, 4).kind(), "isosceles")

    ___ test_isosceles_triangles_have_first_and_last_sides_equal
        assertEqual(Triangle(4, 3, 4).kind(), "isosceles")

    ___ test_isosceles_triangles_have_two_first_sides_equal
        assertEqual(Triangle(4, 4, 3).kind(), "isosceles")

    ___ test_isosceles_triangles_have_in_fact_exactly_two_sides_equal
        assertEqual(Triangle(10, 10, 2).kind(), "isosceles")

    ___ test_scalene_triangles_have_no_equal_sides
        assertEqual(Triangle(3, 4, 5).kind(), "scalene")

    ___ test_scalene_triangles_have_no_equal_sides_at_a_larger_scale_too
        assertEqual(Triangle(10, 11, 12).kind(), "scalene")

        assertEqual(Triangle(5, 4, 2).kind(), "scalene")

    ___ test_very_small_triangles_are_legal
        assertEqual(Triangle(0.4, 0.6, 0.3).kind(), "scalene")

    ___ test_triangles_with_no_size_are_illegal
        assertRaises(TriangleError, Triangle, 0, 0, 0)

    ___ test_triangles_with_negative_sides_are_illegal
        assertRaises(TriangleError, Triangle, 3, 4, -5)

    ___ test_triangles_violating_triangle_inequality_are_illegal
        assertRaises(TriangleError, Triangle, 1, 1, 3)

    ___ test_triangles_violating_triangle_inequality_are_illegal_2
        assertRaises(TriangleError, Triangle, 2, 4, 2)

    ___ test_triangles_violating_triangle_inequality_are_illegal_3
        assertRaises(TriangleError, Triangle, 7, 3, 2)


__ _____ __ _____
    unittest.main()
