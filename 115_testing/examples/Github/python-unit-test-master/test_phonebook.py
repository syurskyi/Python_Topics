import unittest

from phonebook import PhoneBook


class PhoneBookTest(unittest.TestCase):

    # setUp method is inherited from TestCase super class and called BEFORE each test method
    def setUp(self) -> None:
        # construct a new phonebook instance before each test case executes
        self.phonebook = PhoneBook()

    # tearDown method is called AFTER each test method
    # release resources reserved in setUp method OR during test
    # not needed in memory but needed for CI testing of database connection or filesystems
    # def tearDown(self) -> None:
        # pass

    def test_lookup_by_name(self):
        # construct a new phonebook class instance
        # phonebook = PhoneBook()
        # insert new name and number into phonebook
        self.phonebook.add("Bob", "12345")
        # lookup same name I just added
        number = self.phonebook.lookup("Bob")
        # check that the name i've looked up is associated to the number
        # first value is value were checking against, second argument is actual value from unit test
        self.assertEqual("12345", number)

    def test_missing_name(self):
        # assertRaises ensures everything in with context manager will throw a KeyError exception
        # KeyError is raised whenever a dictionary object is requested and the key is not present
        # In our case the name Giles was not present in the phonbook
        with self.assertRaises(KeyError):
            self.phonebook.lookup("Giles")

    # annotation to skip a unittest
    # @unittest.skip("WIP")
    def test_empty_phonebook_is_consistent(self):
        # is_consistent method should return true for empty phonebook
        self.assertTrue(self.phonebook.is_consistent())

    def test_is_consistent_with_different_entries(self):
        # Arrange step to add entries
        # Act step where we check for consistency
        # Assert whether it is or not
        self.phonebook.add("Bob", "12345")
        self.phonebook.add("Anna", "012345")
        self.assertTrue(self.phonebook.is_consistent())

    def test_inconsistent_with_duplicate_entries(self):
        self.phonebook.add("Bob", "12345")
        self.phonebook.add("Sue", "12345")
        self.assertFalse(self.phonebook.is_consistent())

    def test_inconsistent_with_duplicate_prefix(self):
        self.phonebook.add("Bob", "12345")
        self.phonebook.add("Sue", "123")
        self.assertFalse(self.phonebook.is_consistent())

