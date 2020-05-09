______ u__
____ phonebook ______ PhoneBook

# Test runner: >python3 -m unittest -v

# Test Suite
c_ PhoneBookTest?.?
    # Test fixture
    ___ setUp
        phonebook _ PhoneBook()

    # Test fixture
    # Tear down resources that were initialized in setUp
    ___ tearDown
        pass

    # Test case
    ___ test_lookup_by_name # Test case name
        phonebook.add("Bob", "12345") # Arrange
        number _ phonebook.lookup("Bob") # Act
        aE..("12345", number) # Assert

    ___ test_missing_name
        w__ assertRaises(KeyError
            phonebook.lookup("missing")

    ___ test_is_consistent_with_empty_phonebook
        assertTrue(phonebook.is_consistent())

    # Not good test case design. We'll miss a lot of the tests if there is a failure early in the test.
    # Testing stops when an exception is encountered
    # Name of test case isn't specific
    @u__.skip("Bad test case design.")
    ___ test_is_consistent
        phonebook.add("Bob", "12345")
        assertTrue(phonebook.is_consistent())
        phonebook.add("Anna", "012345")
        assertTrue(phonebook.is_consistent())
        phonebook.add("Sue", "12345") # identitcal to Bob
        assertFalse(phonebook.is_consistent())
        phonebook.add("Sue", "123") # prefix of Bob
        assertFalse(phonebook.is_consistent())

    ___ test_is_consistent_with_different_entries
        phonebook.add("Bob", "12345")
        phonebook.add("Anna", "012345")
        assertTrue(phonebook.is_consistent())

    ___ test_inconsistent_with_duplicate_entries
        phonebook.add("Bob", "12345")
        phonebook.add("Sue", "12345")
        assertFalse(phonebook.is_consistent())

    ___ test_inconsistent_with_duplicate_prefix
        phonebook.add("Bob", "12345")
        phonebook.add("Sue", "123")
        assertFalse(phonebook.is_consistent())

    ___ test_phonebook_adds_names_and_numbers
        phonebook.add("Sue", "123343") # Act
        assertIn("Sue", phonebook.get_names()) # Assert made on the same Act
        assertIn("123343", phonebook.get_numbers()) # Assert made on the same Act