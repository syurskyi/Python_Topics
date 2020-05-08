import unittest
from phonebook import Phonebook

c_ PhonebookTest(unittest.TestCase):

    ___ setUp(self):
        self.phonebook = Phonebook()

    ___ test_lookup_entry(self):
        self.phonebook.add("Bob", "12345")
        self.assertEqual("12345", self.phonebook.lookup("Bob"))
