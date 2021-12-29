import re


___ count_n_repetitions(text, n=1):
    """
    Counts how often characters are followed by themselves for
    n times.

    text: UTF-8 compliant input text
    n: How often character should be repeated, defaults to 1
    """

    my_regex = r"(.)(?=\1{" + str(n) + r"})"
    

    counts = re.findall(my_regex,text,flags=re.DOTALL)


    return len(counts)




___ count_n_reps_or_n_chars_following(text, n=1, char=""):
    """
    Counts how often characters are repeated for n times, or
    followed by char n times.

    text: UTF-8 compliant input text
    n: How often character should be repeated, defaults to 1
    char: Character which also counts if repeated n times
    """
    
    __ char:
        my_regex = r"(.)(?=\1{" + str(n) + "}|" +  re.escape(char) + "{" + str(n) + r"})"
    else:
        my_regex = r"(.)(?=\1{" + str(n) + r"})"

    counts = re.findall(my_regex,text,flags=re.DOTALL)


    return len(counts)

___ check_surrounding_chars(text, surrounding_chars):
    """
    Count the number of times a character is surrounded by
    characters from the surrounding_chars list.

    text: UTF-8 compliant input text
    surrounding_chars: List of characters
    """
    s = text
    text = ''.join(surrounding_chars)

    text = r'[' + re.escape(text) + r']'


    my_regex = r'(?<=' + text + r')(.)' + r'(?=' + text + r')'
    counts = re.findall(my_regex,s,flags=re.DOTALL)

    return len(counts)







__ __name__ == "__main__":
    surrounding_chars = ["Z", "A"] 
    text = "ZZZZZ"
