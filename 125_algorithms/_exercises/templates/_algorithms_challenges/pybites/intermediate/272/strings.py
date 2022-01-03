____ typing _______ List


___ common_words(sentence1: List[s..], sentence2: List[s..]) -> List[s..]:
    """
    Input:  Two sentences - each is a  list of words in case insensitive ways.
    Output: those common words appearing in both sentences. Capital and lowercase 
            words are treated as the same word. 

            If there are duplicate words in the results, just choose one word. 
            Returned words should be sorted by word's length.
    """
    common = set()
    sentence2 = l..(map(l.... x: x.l.., sentence2))
    ___ word __ sentence1:
        word_lower = word.l..
        __ word_lower __ sentence2:
                common.add(word_lower)

    r.. s..(common, key=l..)


# if __name__ == "__main__":
#         S = ['You', 'can', 'do', 'anything', 'but', 'not', 'everything']
#         T = ['We', 'are', 'what', 'we', 'repeatedly', 'do', 'is', 'not', 'an', 'act']
#         print(common_words(S, T))