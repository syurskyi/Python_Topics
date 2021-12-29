VOWELS = list('aeiou')


def get_word_max_vowels(text):
   """Get the case insensitive word in text that has most vowels.
      Return a tuple of the matching word and the vowel count, e.g.
      ('object-oriented', 6)"""
   vowel_frequency = {}

   for word in text.split():
      vowel_count = 0
      for char in word:
         if char in VOWELS:
            vowel_count += 1
      if vowel_count > 0:
         vowel_frequency[word] = vowel_count

   vowel_frequency_max = max(vowel_frequency, key=vowel_frequency.get)
   return (vowel_frequency_max, vowel_frequency[vowel_frequency_max])   


# if __name__ == "__main__":
#    test = "Python is an easy to learn, powerful programming language. It has efficient high-level data structures and a simple but effective approach to object-oriented programming. Python’s elegant syntax and dynamic typing, together with its interpreted nature, make it an ideal language for scripting and rapid application development in many areas on most platforms."
#    print(get_word_max_vowels(test))