from phonebook import Phonebook

def test_lookup_entry():
    phonebook = Phonebook()
    phonebook.add("Bob", "12345")
    a__ "12345" == phonebook.lookup("Bob")
