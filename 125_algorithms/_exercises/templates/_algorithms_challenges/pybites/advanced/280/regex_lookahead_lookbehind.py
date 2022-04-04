_______ __


___ count_n_repetitions(text, n=1
    """
    Counts how often characters are followed by themselves for
    n times.

    text: UTF-8 compliant input text
    n: How often character should be repeated, defaults to 1
    """

    my_regex = r"(.)(?=\1{" + s..(n) + r"})"
    

    counts = __.f..(my_regex,text,flags=__.DOTALL)


    r.. l..(counts)




___ count_n_reps_or_n_chars_following(text, n=1, char=""
    """
    Counts how often characters are repeated for n times, or
    followed by char n times.

    text: UTF-8 compliant input text
    n: How often character should be repeated, defaults to 1
    char: Character which also counts if repeated n times
    """
    
    __ char:
        my_regex = r"(.)(?=\1{" + s..(n) + "}|" +  __.escape(char) + "{" + s..(n) + r"})"
    ____
        my_regex = r"(.)(?=\1{" + s..(n) + r"})"

    counts = __.f..(my_regex,text,flags=__.DOTALL)


    r.. l..(counts)

___ check_surrounding_chars(text, surrounding_chars
    """
    Count the number of times a character is surrounded by
    characters from the surrounding_chars list.

    text: UTF-8 compliant input text
    surrounding_chars: List of characters
    """
    s = text
    text = ''.j..(surrounding_chars)

    text = r'[' + __.escape(text) + r']'


    my_regex = r'(?<=' + text + r')(.)' + r'(?=' + text + r')'
    counts = __.f..(my_regex,s,flags=__.DOTALL)

    r.. l..(counts)







__ _______ __ _______
    surrounding_chars = ["Z", "A"] 
    text = "ZZZZZ"
