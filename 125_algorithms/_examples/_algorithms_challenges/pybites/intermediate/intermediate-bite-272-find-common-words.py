"""
Given two sentences that each contains words in case insensitive way, you have to check the
common case insensitive words appearing in both sentences.

If there are duplicate words in the results, just choose one. The results should be
sorted by words length.

The sentences are presented as list of words. Example:

S = ['You', 'can', 'do', 'anything', 'but', 'not', 'everything']
##                  **                       **
T = ['We', 'are', 'what', 'we', 'repeatedly', 'do', 'is', 'not', 'an', 'act']
##                                             **          **
Result = ['do', 'not']
"""

from typing import List


def common_words(sentence1: List[str], sentence2: List[str]) -> List[str]:
    """
    Input:  Two sentences - each is a  list of words in case insensitive ways.
    Output: those common words appearing in both sentences. Capital and lowercase
            words are treated as the same word.

            If there are duplicate words in the results, just choose one word.
            Returned words should be sorted by word's length.
    """
    lower_s1 = [e.lower() for e in sentence1 ]
    lower_s2 = [e.lower() for e in sentence2 ]
    result = list(set(lower_s1) & set(lower_s2))

    return sorted(result, key=len)

"""
Approach:

First, eliminate duplicates within each sentence.
Second, use a intersection on both lists to find common elements.
"""

sentence1 = ['To', 'be', 'or', 'not', 'to', 'be',
             'that', 'is', 'a', 'question']
sentence2 = ['To', 'strive', 'to', 'seek', 'to',
             'find', 'and', 'not', 'to', 'yield']
sentence3 = ['No', 'two', 'persons', 'ever', 'to',
             'read', 'the', 'same', 'book', 'You', 'said']
sentence4 = ['The', 'more', 'read', 'the',
             'more', 'things', 'will', 'know']
sentence5 = ['be', 'a', 'good', 'man']

print(common_words(sentence1, sentence5))

