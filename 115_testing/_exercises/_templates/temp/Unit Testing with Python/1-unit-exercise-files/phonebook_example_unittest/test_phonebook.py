#
# ______ u__
#
# ____ p.. ______ P..
#
# c_ PhonebookTest?.?
#
#     ___ setUp
#         phonebook _ ?
#
#     ___ test_lookup_entry_by_name
#         ?.a.. "Bob", "12345"
#         aE.. "12345", ?.l.. "Bob"
#
#     ___ test_missing_entry_raises_KeyError
#         w__ aR.. K..
#             ?.l.. "missing"
#
#     ___ test_empty_phonebook_is_consistent
#         aT..(?.i_c..
#
#     ??.s.. "poor example"
#     ___ test_is_consistent
#         aT.. ?.i_c..
#         ?.a.. "Bob", "12345"
#         aT.. ?.i_c..
#         ?.a.. "Mary", "012345"
#         aT.. ?.i_c..
#         ?.a.. "Sue", "12345" # identical to Bob
#         aF.. ?.i_c..
#         ?.a.. "Sue", "123" # prefix of Bob
#         aF..(?.i_c..
#
#     ___ test_phonebook_with_normal_entries_is_consistent
#         ?.a.. "Bob", "12345"
#         ?.a.. "Mary", "012345"
#         aT.. ?.i_c..
#
#     ___ test_phonebook_with_duplicate_entries_is_inconsistent
#         ?.a.. "Bob", "12345"
#         ?.a.. "Mary", "12345"
#         aF.. ?.i_c..
#
#     ___ test_phonebook_with_numbers_that_prefix_one_another_is_inconsistent
#         ?.a.. "Bob" "12345"
#         ?.a.. "Mary" "123"
#         aF.. ?.i_c..
#
#     ___ test_phonebook_adds_names_and_numbers
#         ?.a.. "Sue", "12345"
#         aI.. "Sue", ?.g_n..
#         aI.. "12345", ?.g_nu..
#
#
#
#