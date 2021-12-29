def is_anagram(word1, word2):
   """Receives two words and returns True/False (boolean) if word2 is
      an anagram of word1.
      About anagrams: https://en.wikipedia.org/wiki/Anagram"""
   word1 = word1.replace(" ", "").lower()
   word2 = word2.replace(" ", "").lower()
   if sorted(word1) == sorted(word2):
      return True
   else:
      return False


# if __name__ == "__main__":
#    print(is_anagram("restful", "fluster"))