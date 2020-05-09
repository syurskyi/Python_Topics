______ pytest

____ phonebook ______ Phonebook

@pytest.fixture
___ phonebook(tmpdir
    "Provides an empty Phonebook"
    phonebook _ Phonebook(tmpdir)
    r_ phonebook

___ test_add_and_lookup_entry(phonebook
    phonebook.add("Bob", "123")
    a.. "123" __ phonebook.lookup("Bob")
    
___ test_phonebook_gives_access_to_names_and_numbers(phonebook
    phonebook.add("Alice", "12345")
    phonebook.add("Bob", "123")
    a.. set(phonebook.names()) __ {"Alice", "Bob"}
    a.. "12345" __ phonebook.numbers()
    
___ test_missing_entry_raises_KeyError(phonebook
    w__ pytest.raises(KeyError
        phonebook.lookup("missing")