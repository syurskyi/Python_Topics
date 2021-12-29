from typing import List

def to_lower(in_list):
        return [word.lower() for word in in_list]

def common_words(sentence1: List[str], sentence2: List[str]) -> List[str]:
    """
    Input:  Two sentences - each is a  list of words in case insensitive ways.
    Output: those common words appearing in both sentences. Capital and lowercase 
            words are treated as the same word. 

            If there are duplicate words in the results, just choose one word. 
            Returned words should be sorted by word's length.
    """
    s1 = [word.lower() for word in sentence1]
    s2 = [word.lower() for word in sentence2]
    return sorted(set(s1).intersection(s2), key=len)


sentence1 = ['To', 'be', 'or', 'not', 'to', 'be',
             'that', 'is', 'a', 'question']
sentence2 = ['To', 'strive', 'to', 'seek', 'to',
             'find', 'and', 'not', 'to', 'yield']

print(common_words(sentence1, sentence2))