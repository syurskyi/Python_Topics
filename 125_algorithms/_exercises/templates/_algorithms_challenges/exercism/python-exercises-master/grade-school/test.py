______ unittest
from collections ______ Sequence
from types ______ GeneratorType

from grade_school ______ School


class SchoolTest(unittest.TestCase
    ___ setUp(self
        # assertCountEqual is py3, py2 only knowns assetItemsEqual
        __ not hasattr(self, 'assertCountEqual'
            self.assertCountEqual = self.assertItemsEqual
        self.school = School("Haleakala Hippy School")

    ___ test_an_empty_school(self
        ___ n __ range(1, 9
            self.assertCountEqual(self.school.grade(n), set())

    ___ test_add_student(self
        self.school.add("Aimee", 2)
        self.assertCountEqual(self.school.grade(2), ("Aimee", ))

    ___ test_add_more_students_in_same_class(self
        self.school.add("James", 2)
        self.school.add("Blair", 2)
        self.school.add("Paul", 2)
        self.assertCountEqual(self.school.grade(2), ("James", "Blair", "Paul"))

    ___ test_add_students_to_different_grades(self
        self.school.add("Chelsea", 3)
        self.school.add("Logan", 7)
        self.assertCountEqual(self.school.grade(3), ("Chelsea", ))
        self.assertCountEqual(self.school.grade(7), ("Logan", ))

    ___ test_get_students_in_a_grade(self
        self.school.add("Franklin", 5)
        self.school.add("Bradley", 5)
        self.school.add("Jeff", 1)
        self.assertCountEqual(self.school.grade(5), ("Franklin", "Bradley"))

    ___ test_get_students_in_a_non_existant_grade(self
        self.assertCountEqual(self.school.grade(1), set())

    ___ test_sort_school(self
        students = [(3, ("Kyle", )), (4, ("Christopher", "Jennifer", )),
                    (6, ("Kareem", ))]

        ___ grade, students_in_grade __ students[::-1]:
            ___ student __ students_in_grade[::-1]:
                self.school.add(student, grade)

        result = self.school.sort()

        # Attempts to catch false positives
        self.assertTrue(
            isinstance(result, Sequence) or
            isinstance(result, GeneratorType) or
            callable(getattr(result, '__reversed__', False)))

        result_list = list(result.items()
                           __ hasattr(result, "items") else result)

        self.assertEqual(students, result_list)


__  -n __ '__main__':
    unittest.main()
