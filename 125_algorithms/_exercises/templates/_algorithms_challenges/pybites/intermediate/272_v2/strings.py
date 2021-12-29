____ typing _______ List


___ common_words(sentence1: List[str], sentence2: List[str]) -> List[str]:
    """
    Input:  Two sentences - each is a  list of words in case insensitive ways.
    Output: those common words appearing in both sentences. Capital and lowercase 
            words are treated as the same word. 

            If there are duplicate words in the results, just choose one word. 
            Returned words should be sorted by word's length.
    """



    r.. s..(l..(set(word.lower() ___ word __ sentence1) & set(word.lower() ___ word __ sentence2)),key=l..)
