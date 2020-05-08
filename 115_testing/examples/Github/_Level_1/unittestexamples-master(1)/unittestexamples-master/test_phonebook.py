import unittest
from phonebook import PhoneBook

# Test runner: >python3 -m unittest -v

# Test Suite
class PhoneBookTest(unittest.TestCase):
    # Test fixture
    def setUp(self):
        self.phonebook = PhoneBook()

    # Test fixture
    # Tear down resources that were initialized in setUp
    def tearDown(self):
        pass

    # Test case
    def test_lookup_by_name(self): # Test case name
        self.phonebook.add("Bob", "12345") # Arrange
        number = self.phonebook.lookup("Bob") # Act
        self.assertEqual("12345", number) # Assert

    def test_missing_name(self):
        with self.assertRaises(KeyError):
            self.phonebook.lookup("missing")

    def test_is_consistent_with_empty_phonebook(self):
        self.assertTrue(self.phonebook.is_consistent())

    # Not good test case design. We'll miss a lot of the tests if there is a failure early in the test.
    # Testing stops when an exception is encountered
    # Name of test case isn't specific
    @unittest.skip("Bad test case design.")
    def test_is_consistent(self):
        self.phonebook.add("Bob", "12345")
        self.assertTrue(self.phonebook.is_consistent())
        self.phonebook.add("Anna", "012345")
        self.assertTrue(self.phonebook.is_consistent())
        self.phonebook.add("Sue", "12345") # identitcal to Bob
        self.assertFalse(self.phonebook.is_consistent())
        self.phonebook.add("Sue", "123") # prefix of Bob
        self.assertFalse(self.phonebook.is_consistent())

    def test_is_consistent_with_different_entries(self):
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

    def test_phonebook_adds_names_and_numbers(self):
        self.phonebook.add("Sue", "123343") # Act
        self.assertIn("Sue", self.phonebook.get_names()) # Assert made on the same Act
        self.assertIn("123343", self.phonebook.get_numbers()) # Assert made on the same Act