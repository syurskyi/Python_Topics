___ anagrams(word, words):
    return [w for w in words __ sorted(w) == sorted(word)]

print(anagrams('aabb',['aabb','bbaa','ccaa','baba']))
