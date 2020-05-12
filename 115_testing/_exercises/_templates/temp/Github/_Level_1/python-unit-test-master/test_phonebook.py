______ u__

____ phonebook ______ PhoneBook


c_ PhoneBookTest?.?

    # setUp method is inherited from TestCase super class and called BEFORE each test method
    ___ setUp(self)  N..:
        # construct a new phonebook instance before each test case executes
        phonebook _ PhoneBook()

    # tearDown method is called AFTER each test method
    # release resources reserved in setUp method OR during test
    # not needed in memory but needed for CI testing of database connection or filesystems
    # def tearDown(self) -> None:
        # pass

    ___ test_lookup_by_name
        # construct a new phonebook class instance
        # phonebook = PhoneBook()
        # insert new name and number into phonebook
        phonebook.add("Bob", "12345")
        # lookup same name I just added
        number _ phonebook.l..("Bob")
        # check that the name i've looked up is associated to the number
        # first value is value were checking against, second argument is actual value from unit test
        aE..("12345", number)

    ___ test_missing_name
        # assertRaises ensures everything in with context manager will throw a KeyError exception
        # KeyError is raised whenever a dictionary object is requested and the key is not present
        # In our case the name Giles was not present in the phonbook
        w__ aR..(K..
            phonebook.l..("Giles")

    # annotation to skip a unittest
    # @unittest.skip("WIP")
    ___ test_empty_phonebook_is_consistent
        # is_consistent method should return true for empty phonebook
        aT..(phonebook.i_c..())

    ___ test_is_consistent_with_different_entries
        # Arrange step to add entries
        # Act step where we check for consistency
        # Assert whether it is or not
        phonebook.add("Bob", "12345")
        phonebook.add("Anna", "012345")
        aT..(phonebook.i_c..())

    ___ test_inconsistent_with_duplicate_entries
        phonebook.add("Bob", "12345")
        phonebook.add("Sue", "12345")
        aF..(phonebook.i_c..())

    ___ test_inconsistent_with_duplicate_prefix
        phonebook.add("Bob", "12345")
        phonebook.add("Sue", "123")
        aF..(phonebook.i_c..())

