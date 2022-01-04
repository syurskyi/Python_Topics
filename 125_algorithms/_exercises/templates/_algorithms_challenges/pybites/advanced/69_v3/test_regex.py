____ regex _______ (has_timestamp, is_integer,
                   has_word_with_dashes, remove_all_parenthesis_words,
                   split_string_on_punctuation, remove_duplicate_spacing,
                   has_three_consecutive_vowels,
                   convert_emea_date_to_amer_date)


___ test_has_timestamp
    ... has_timestamp('INFO 2014-07-03T23:27:51 Shutdown initiated.')
    ... has_timestamp('INFO 2014-06-01T13:28:51 Shutdown initiated.')
    ... n.. has_timestamp('INFO 2014-7-3T23:27:51 Shutdown initiated.')
    ... n.. has_timestamp('INFO 2014-07-03t23:27:1 Shutdown initiated.')


___ test_is_integer
    ... is_integer(1)
    ... is_integer(-1)
    ... n.. is_integer('str')
    ... n.. is_integer(1.1)


___ test_has_word_with_dashes
    ... has_word_with_dashes('this Bite is self-contained')
    ... has_word_with_dashes('the match ended in 1-1')
    ... n.. has_word_with_dashes('this Bite is not selfcontained')
    ... n.. has_word_with_dashes('the match ended in 1- 1')


___ test_remove_all_parenthesis_words
    input_string = 'good morning (afternoon), how are you?'
    expected = 'good morning, how are you?'
    ... remove_all_parenthesis_words(input_string) __ expected
    input_string = 'math (8.6) and science (9.1) where his strengths'
    expected = 'math and science where his strengths'
    ... remove_all_parenthesis_words(input_string) __ expected


___ test_split_string_on_punctuation
    input_string = 'hi, how are you doing? blabla'
    expected = ['hi', 'how are you doing', 'blabla']
    ... split_string_on_punctuation(input_string) __ expected
    input_string = ';String. with. punctuation characters!'
    expected = ['String', 'with', 'punctuation characters']
    ... split_string_on_punctuation(input_string) __ expected


___ test_remove_duplicate_spacing
    input_string = 'This is a   string with  too    much spacing'
    expected = 'This is a string with too much spacing'
    ... remove_duplicate_spacing(input_string) __ expected


___ test_has_three_consecutive_vowels
    ... has_three_consecutive_vowels('beautiful')
    ... has_three_consecutive_vowels('queueing')
    ... n.. has_three_consecutive_vowels('mountain')
    ... n.. has_three_consecutive_vowels('house')


___ test_convert_emea_date_to_amer_date
    ... convert_emea_date_to_amer_date('31/03/2018') __ '03/31/2018'
    ... convert_emea_date_to_amer_date('none') __ 'none'