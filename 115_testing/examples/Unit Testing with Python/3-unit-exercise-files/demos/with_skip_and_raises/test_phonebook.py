import pytest

from phonebook import Phonebook

def test_add_and_lookup_entry():
    pytest.skip("WIP")
    phonebook = Phonebook()
    phonebook.add("Bob", "123")
    a__ "123" == phonebook.lookup("Bob")
    
def test_phonebook_gives_access_to_names_and_numbers():
    phonebook = Phonebook()
    phonebook.add("Alice", "12345")
    phonebook.add("Bob", "123")
    a__ set(phonebook.names()) == {"Alice", "Bob"}
    a__ "12345" in phonebook.numbers()
    
def test_missing_entry_raises_KeyError():
    phonebook = Phonebook()
    with pytest.raises(KeyError):
        phonebook.lookup("missing")