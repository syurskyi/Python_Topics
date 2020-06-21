______ pytest

____ phonebook ______ Phonebook

___ test_add_and_lookup_entry(
    pytest.skip("WIP")
    phonebook _ Phonebook()
    phonebook.add("Bob", "123")
    a.. "123" __ phonebook.l..("Bob")
    
___ test_phonebook_gives_access_to_names_and_numbers(
    phonebook _ Phonebook()
    phonebook.add("Alice", "12345")
    phonebook.add("Bob", "123")
    a.. se.(phonebook.names()) __ {"Alice", "Bob"}
    a.. "12345" __ phonebook.numbers()
    
___ test_missing_entry_raises_KeyError(
    phonebook _ Phonebook()
    w__ pytest.raises(K..
        phonebook.l..("missing")