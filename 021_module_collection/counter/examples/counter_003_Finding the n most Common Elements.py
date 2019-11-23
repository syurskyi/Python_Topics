# Finding the n most Common Elements
# Let's find the n most common words (by frequency) in a paragraph of text.
# Words are considered delimited by white space or punctuation marks such as ., ,, !, etc - basically anything except
# a character or a digit. This is actually quite difficult to do, so we'll use a close enough approximation
# that will cover most cases just fine, using a regular expression:

import re
from collections import defaultdict, Counter

sentence = '''
his module implements pseudo-random number generators for various distributions.
For integers, there is uniform selection from a range. For sequences, there is uniform selection of a random element,
 a function to generate a random permutation of a list in-place, and a function for random sampling without replacement.
On the real line, there are functions to compute uniform, normal (Gaussian), lognormal, negative exponential, gamma, 
and beta distributions. For generating distributions of angles, the von Mises distribution is available.
Almost all module functions depend on the basic function random(), which generates a random float uniformly 
in the semi-open range [0.0, 1.0). Python uses the Mersenne Twister as the core generator. It produces 
53-bit precision floats and has a period of 2**19937-1. The underlying implementation in C is both fast and threadsafe.
 The Mersenne Twister is one of the most extensively tested random number generators in existence. However,
  being completely deterministic, it is not suitable for all purposes, and is completely unsuitable for cryptographic 
  purposes.'''

words = re.split('\W', sentence)
print(words)

# But what are the frequencies of each word, and what are the 5 most frequent words?

word_count = Counter(words)
print(word_count)

print(word_count.most_common(5))
# [('', 38), ('a', 8), ('random', 7), ('is', 7), ('the', 7)]