______ pytest

____ phonebook ______ Phonebook

@pytest.fixture
___ phonebook(request
    phonebook _ Phonebook()
    ___ cleanup_phonebook(
        phonebook.clear()
    request.addfinalizer(cleanup_phonebook)
    r_ phonebook

___ test_add_and_lookup_entry(phonebook
    phonebook.add("Bob", "123")
    a.. "123" __ phonebook.l..("Bob")
    
___ test_phonebook_gives_access_to_names_and_numbers(phonebook
    phonebook.add("Alice", "12345")
    phonebook.add("Bob", "123")
    a.. se.(phonebook.names()) __ {"Alice", "Bob"}
    a.. "12345" __ phonebook.numbers()
    
___ test_missing_entry_raises_KeyError(phonebook
    w__ pytest.raises(K..
        phonebook.l..("missing")