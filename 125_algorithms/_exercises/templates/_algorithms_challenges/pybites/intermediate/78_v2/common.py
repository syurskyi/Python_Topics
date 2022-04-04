___ common_languages(programmers
   """Receive a dict of keys -> names and values -> a sequence of
      of programming languages, return the common languages"""
   common = s..()

   ___ i __ r..(l..(programmers:
      ___ key, value __ programmers.i..:
         __ i __ 1:
            common.update(value)
         common = common.intersection(value)
   r.. common


# if __name__ == "__main__":

#    devs = dict(bob=['JS', 'PHP', 'Python', 'Perl', 'Java'],
#                 tim=['Python', 'Haskell', 'C++', 'JS'],
#                 sara=['Perl', 'C', 'Java', 'Python', 'JS'],
#                 paul=['C++', 'JS', 'Python'])

#    common_languages(devs)