from phonebook import Phonebook

def test_lookup_entry():
    phonebook = Phonebook()
    phonebook.add("Bob", "12345")
    assert "12345" == phonebook.lookup("Bob")
