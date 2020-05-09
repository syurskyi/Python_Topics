______ unittest
____ phonebook ______ Phonebook

c_ PhonebookTest(unittest.TestCase):

    ___ setUp
        phonebook _ Phonebook()

    ___ test_lookup_entry
        phonebook.add("Bob", "12345")
        assertEqual("12345", phonebook.lookup("Bob"))
