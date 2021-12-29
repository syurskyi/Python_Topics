____ typing _______ List

___ to_lower(in_list):
        r.. [word.lower() ___ word __ in_list]

___ common_words(sentence1: List[s..], sentence2: List[s..]) -> List[s..]:
    """
    Input:  Two sentences - each is a  list of words in case insensitive ways.
    Output: those common words appearing in both sentences. Capital and lowercase 
            words are treated as the same word. 

            If there are duplicate words in the results, just choose one word. 
            Returned words should be sorted by word's length.
    """
    s1 = [word.lower() ___ word __ sentence1]
    s2 = [word.lower() ___ word __ sentence2]
    r.. s..(set(s1).intersection(s2), key=l..)


sentence1 = ['To', 'be', 'or', 'not', 'to', 'be',
             'that', 'is', 'a', 'question']
sentence2 = ['To', 'strive', 'to', 'seek', 'to',
             'find', 'and', 'not', 'to', 'yield']

print(common_words(sentence1, sentence2))