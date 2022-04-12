___ get_duplicate_indices(words
   """Given a list of words, loop through the words and check for each
      word if it occurs more than once.
      If so return the index of its first occurrence.
      For example in the following list 'is' and 'it'
      occur more than once, and they are at indices 0 and 1 so you would
      return [0, 1]:
      ['is', 'it', 'true', 'or', 'is', 'it', 'not?'] => [0, 1]
      Make sure the returning list is unique and sorted in ascending order."""
   duplicate_index    # dict

   ___ i __ r..(l..(words:
      ___ j __ r..(l..(words:
         __ i !_ j a.. words[i] __ words[j]:
            __ words[i] n.. __ duplicate_index:
               duplicate_index[words[i]] i

   r.. [value ___ value __ duplicate_index.v..

   
# if __name__ == "__main__":
#    print(get_duplicate_indices(['is', 'it', 'true', 'or', 'is', 'it', 'not?']))