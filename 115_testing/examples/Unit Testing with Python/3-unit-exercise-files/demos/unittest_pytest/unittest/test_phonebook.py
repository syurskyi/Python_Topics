import unittest
from phonebook import Phonebook

class PhonebookTest(unittest.TestCase):

    def setUp(self):
        self.phonebook = Phonebook()

    def test_lookup_entry(self):
        self.phonebook.add("Bob", "12345")
        self.assertEqual("12345", self.phonebook.lookup("Bob"))
