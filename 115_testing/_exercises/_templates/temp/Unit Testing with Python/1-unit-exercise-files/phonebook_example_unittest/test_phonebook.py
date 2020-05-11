
______ u__

____ phonebook ______ Phonebook

c_ PhonebookTest?.?
    
    ___ setUp
        phonebook _ Phonebook()
    
    ___ test_lookup_entry_by_name
        phonebook.add("Bob", "12345")
        aE..("12345", phonebook.lookup("Bob"))
        
    ___ test_missing_entry_raises_KeyError
        w__ aR..(KeyError
            phonebook.lookup("missing")
            
    ___ test_empty_phonebook_is_consistent
        aT..(phonebook.is_consistent())
        
    @u__.skip("poor example")
    ___ test_is_consistent
        aT..(phonebook.is_consistent())
        phonebook.add("Bob", "12345")
        aT..(phonebook.is_consistent())
        phonebook.add("Mary", "012345")
        aT..(phonebook.is_consistent())
        phonebook.add("Sue", "12345") # identical to Bob
        aF..(phonebook.is_consistent())
        phonebook.add("Sue", "123") # prefix of Bob
        aF..(phonebook.is_consistent())
        
    ___ test_phonebook_with_normal_entries_is_consistent
        phonebook.add("Bob", "12345")
        phonebook.add("Mary", "012345")
        aT..(phonebook.is_consistent())

    ___ test_phonebook_with_duplicate_entries_is_inconsistent
        phonebook.add("Bob", "12345")
        phonebook.add("Mary", "12345")
        aF..(phonebook.is_consistent())
        
    ___ test_phonebook_with_numbers_that_prefix_one_another_is_inconsistent
        phonebook.add("Bob", "12345")
        phonebook.add("Mary", "123")
        aF..(phonebook.is_consistent())
        
    ___ test_phonebook_adds_names_and_numbers
        phonebook.add("Sue", "12345")
        aI..("Sue", phonebook.get_names())
        aI..("12345", phonebook.get_numbers())
        
        
        
    