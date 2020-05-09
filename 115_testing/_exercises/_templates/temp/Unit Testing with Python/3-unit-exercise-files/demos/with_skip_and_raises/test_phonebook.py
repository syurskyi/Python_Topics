______ pytest

____ phonebook ______ Phonebook

___ test_add_and_lookup_entry():
    pytest.skip("WIP")
    phonebook _ Phonebook()
    phonebook.add("Bob", "123")
    assert "123" == phonebook.lookup("Bob")
    
___ test_phonebook_gives_access_to_names_and_numbers():
    phonebook _ Phonebook()
    phonebook.add("Alice", "12345")
    phonebook.add("Bob", "123")
    assert set(phonebook.names()) == {"Alice", "Bob"}
    assert "12345" in phonebook.numbers()
    
___ test_missing_entry_raises_KeyError():
    phonebook _ Phonebook()
    with pytest.raises(KeyError):
        phonebook.lookup("missing")