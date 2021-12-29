from typing import List


___ common_words(sentence1: List[str], sentence2: List[str]) -> List[str]:
    """
    Input:  Two sentences - each is a  list of words in case insensitive ways.
    Output: those common words appearing in both sentences. Capital and lowercase 
            words are treated as the same word. 

            If there are duplicate words in the results, just choose one word. 
            Returned words should be sorted by word's length.
    """
    common = set()
    sentence2 = list(map(lambda x: x.lower(), sentence2))
    for word in sentence1:
        word_lower = word.lower()
        __ word_lower in sentence2:
                common.add(word_lower)

    return sorted(common, key=len)


# if __name__ == "__main__":
#         S = ['You', 'can', 'do', 'anything', 'but', 'not', 'everything']
#         T = ['We', 'are', 'what', 'we', 'repeatedly', 'do', 'is', 'not', 'an', 'act']
#         print(common_words(S, T))