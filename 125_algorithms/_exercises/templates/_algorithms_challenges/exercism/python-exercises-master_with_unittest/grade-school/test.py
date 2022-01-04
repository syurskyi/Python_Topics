_______ unittest
____ c.. _______ Sequence
____ types _______ GeneratorType

____ grade_school _______ School


c_ SchoolTest(unittest.TestCase):
    ___ setUp
        # assertCountEqual is py3, py2 only knowns assetItemsEqual
        __ n.. hasattr(self, 'assertCountEqual'):
            assertCountEqual = assertItemsEqual
        school = School("Haleakala Hippy School")

    ___ test_an_empty_school
        ___ n __ r..(1, 9):
            assertCountEqual(school.grade(n), set())

    ___ test_add_student
        school.add("Aimee", 2)
        assertCountEqual(school.grade(2), ("Aimee", ))

    ___ test_add_more_students_in_same_class
        school.add("James", 2)
        school.add("Blair", 2)
        school.add("Paul", 2)
        assertCountEqual(school.grade(2), ("James", "Blair", "Paul"))

    ___ test_add_students_to_different_grades
        school.add("Chelsea", 3)
        school.add("Logan", 7)
        assertCountEqual(school.grade(3), ("Chelsea", ))
        assertCountEqual(school.grade(7), ("Logan", ))

    ___ test_get_students_in_a_grade
        school.add("Franklin", 5)
        school.add("Bradley", 5)
        school.add("Jeff", 1)
        assertCountEqual(school.grade(5), ("Franklin", "Bradley"))

    ___ test_get_students_in_a_non_existant_grade
        assertCountEqual(school.grade(1), set())

    ___ test_sort_school
        students = [(3, ("Kyle", )), (4, ("Christopher", "Jennifer", )),
                    (6, ("Kareem", ))]

        ___ grade, students_in_grade __ students[::-1]:
            ___ student __ students_in_grade[::-1]:
                school.add(student, grade)

        result = school.s..()

        # Attempts to catch false positives
        assertTrue(
            isi..(result, Sequence) o.
            isi..(result, GeneratorType) o.
            callable(getattr(result, '__reversed__', F..)))

        result_list = l..(result.i..
                           __ hasattr(result, "items") ____ result)

        assertEqual(students, result_list)


__ _____ __ _____
    unittest.main()
