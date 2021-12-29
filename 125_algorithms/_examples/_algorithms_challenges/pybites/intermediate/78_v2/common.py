def common_languages(programmers):
   """Receive a dict of keys -> names and values -> a sequence of
      of programming languages, return the common languages"""
   common = set()

   for i in range(len(programmers)):
      for key, value in programmers.items():
         if i == 1:
            common.update(value)
         common = common.intersection(value)
   return common


# if __name__ == "__main__":

#    devs = dict(bob=['JS', 'PHP', 'Python', 'Perl', 'Java'],
#                 tim=['Python', 'Haskell', 'C++', 'JS'],
#                 sara=['Perl', 'C', 'Java', 'Python', 'JS'],
#                 paul=['C++', 'JS', 'Python'])

#    common_languages(devs)