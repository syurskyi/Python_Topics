# ____ ? _______ (has_timestamp, is_integer,
#                    has_word_with_dashes, remove_all_parenthesis_words,
#                    split_string_on_punctuation, remove_duplicate_spacing,
#                    has_three_consecutive_vowels,
#                    convert_emea_date_to_amer_date)
#
#
# ___ test_has_timestamp
#     ...  ? 'INFO 2014-07-03T23:27:51 Shutdown initiated.'
#     ...  ? 'INFO 2014-06-01T13:28:51 Shutdown initiated.'
#     ... n..  ? 'INFO 2014-7-3T23:27:51 Shutdown initiated.'
#     ... n..  ? 'INFO 2014-07-03t23:27:1 Shutdown initiated.'
#
#
# ___ test_is_integer
#     ...  ? 1
#     ...  ? -1
#     ... n..  ? 'str'
#     ... n..  ? 1.1
#
#
# ___ test_has_word_with_dashes
#     ...  ? 'this Bite is self-contained'
#     ...  ? 'the match ended in 1-1'
#     ... n..  ? 'this Bite is not selfcontained'
#     ... n..  ? 'the match ended in 1- 1'
#
#
# ___ test_remove_all_parenthesis_words
#     input_string 'good morning (afternoon), how are you?'
#     e.. 'good morning, how are you?'
#     ... ? ? __ e..
#     input_string 'math (8.6) and science (9.1) where his strengths'
#     e.. 'math and science where his strengths'
#     ... ? ? __ e..
#
#
# ___ test_split_string_on_punctuation
#     input_string 'hi, how are you doing? blabla'
#     e.. =  'hi', 'how are you doing', 'blabla'
#     ... ? ? __ e..
#     input_string ';String. with. punctuation characters!'
#     e.. =  'String', 'with', 'punctuation characters'
#     ... ? ? __ e..
#
#
# ___ test_remove_duplicate_spacing
#     input_string 'This is a   string with  too    much spacing'
#     e.. 'This is a string with too much spacing'
#     ... ? ? __ e..
#
#
# ___ test_has_three_consecutive_vowels
#     ... ? 'beautiful'
#     ... ? 'queueing'
#     ... n.. ? 'mountain'
#     ... n.. ? 'house'
#
#
# ___ test_convert_emea_date_to_amer_date
#     ... ? '31/03/2018') __ '03/31/2018'
#     ... ? 'none') __ 'none'